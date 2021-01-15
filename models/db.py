from flask_sqlalchemy import SQLAlchemy
from models.payment_options import PaymentOption
import datetime
import json

db = SQLAlchemy()

def addClient(customer):
    db.session.add(customer)
    db.session.commit()

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
        # return {
        #     column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
        #     for column, value in self._to_dict().items()
        # }

    @staticmethod
    def getId(objType,id):
        obj = objType.__class__.query.get(id)
        return obj

class Customers(BaseModel):
    __tablename__ = 'customers'

    id = db.Column(db.Integer,primary_key=True)
    full_name = db.Column(db.String)
    phone_number = db.Column(db.Integer)
    payment_type = db.Column(db.Enum(PaymentOption))
    payment_tag = db.Column(db.String)
    payment_amount = db.Column(db.Integer)
    payment_date = db.Column(db.Date) 
    email_address = db.Column(db.String)
    last_payment = db.Column(db.Date)
    active = db.Column(db.Boolean)

    def __init__(self, full_name, phone_number , email_address, payment_type=None, payment_tag=None, payment_amount=None , payment_date=None,  last_payment=None, active=False):
        self.full_name = full_name 
        self.phone_number = phone_number
        self.payment_type = payment_type
        self.payment_tag = payment_tag 
        self.payment_amount = payment_amount
        self.payment_date = payment_date
        self.email_address = email_address
        self.last_payment = last_payment 
        self.active = active

    def __repr__(self):
        return '<id {} name {}>'.format(self.id,self.full_name)
