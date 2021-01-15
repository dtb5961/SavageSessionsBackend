from flask import Flask,request
from models.db import db as db
from models.db import Customers
from models.payment_options import PaymentOption
import sys


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tester:tester@localhost:5432/SavageSessions' 
db.init_app(app)

@app.route('/')
def main():
    return 'Hello World'

@app.route('/new_customer', methods=['POST'])
def addCustomer():
    data = request.get_json(force=True)
    
    if data.get('payment_type') != None:
        data['payment_type'] = PaymentOption(data['payment_type'])
    
    newUser = Customers(**data)
    
    try:
        db.session.add(newUser)
        db.session.commit()
        return newUser.json(), 200
    except Exception as e:
        return str(e), 409

@app.route('/get_customer/<id>', methods=['GET'])
def getCustomer(id):
    try:
        customer = getCustomerDB(id)
        return customer.json(), 200

    except Exception as e:
        return str(e), 400


@app.route('/update_customer',methods=['PUT'])
def updateCustomer():
    data = request.get_json(force=True)
    if(data.get('id') == None):
        return "Request Must Have ID", 400
    else:
        currentCustomer = getCustomerDB(data.get('id'))
        for k,v in data.items():
            if data.get(k) != currentCustomer.json().get(k):
                setattr(currentCustomer,k,v)
        
        db.session.commit()
    return '',200


def getCustomerDB(id):
    return Customers.query.get(id)

if __name__ == '__main__':
    app.run()

