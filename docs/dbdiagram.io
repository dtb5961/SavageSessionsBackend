//// -- LEVEL 1
//// -- Tables and References

// Creating tables
Table customers as U {
  id int [pk, increment] // auto-increment
  first_name varchar
  last_name varchar
  phone_number varchar
  payment_option enum
  payment_tag varchar
  payment_amount numeric
  payment_date date
  email_address varchar
  last_payment date
  active boolean
}


CREATE TYPE payment_option AS ENUM ('zelle','cashapp','cash','other')