CREATE DATABASE SavageSessions;
GRANT ALL PRIVILEGES ON DATABASE SavageSessions TO tester;

DROP TABLE IF EXISTS customers;
DROP TYPE IF EXISTS pay_options;
CREATE TYPE pay_options AS ENUM ('Zelle','CashApp','Cash','Other');

CREATE TABLE customers(
  id SERIAL PRIMARY KEY,
  full_name VARCHAR(70) UNIQUE NOT NULL,
  phone_number VARCHAR(10),
  payment_type pay_options,
  payment_tag VARCHAR(50),
  payment_amount INTEGER,
  payment_date TIMESTAMP,
  email_address VARCHAR(50),
  last_payment TIMESTAMP,
  active BOOLEAN
);


