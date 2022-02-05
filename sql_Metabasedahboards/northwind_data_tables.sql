DROP TABLE if exists categories;
CREATE TABLE categories
(categoryId float primary key,
categoryName varchar(40) unique,
description varchar(140),
picture float);
\copy categories FROM 'C:\Users\mahas\Desktop\spiced_projects\week5\northwind_data_clean\data\categories.csv' DELIMITER ',' CSV HEADER;

DROP TABLE if exists customers;
CREATE TABLE customers
(customerId varchar(140) primary key,
companyName varchar(140),
contactName varchar(140),
contactTitle varchar(140),
address varchar(140),
city varchar(140),
region varchar(140),
postatlCode varchar(140),
country varchar(50),
phone varchar(20),
fax varchar(30));
\copy customers FROM 'C:\Users\mahas\Desktop\spiced_projects\week5\northwind_data_clean\data\customers.csv' DELIMITER ',' CSV HEADER;

DROP TABLE if exists employee_territories;
CREATE TABLE employee_territories
(employeeId float,
territoyId float primary key);
\copy employee_territories FROM 'C:\Users\mahas\Desktop\spiced_projects\week5\northwind_data_clean\data\employee_territories.csv' DELIMITER ',' CSV HEADER;

DROP TABLE if exists employees;
CREATE TABLE employees
(employeeId float primary key,
lastName varchar(50),
firstName varchar(50),
title varchar(50),
titleOfCourtesy varchar(50),
birthDate date,
hireDate date,
address varchar(70),
city varchar(30),
region varchar(40),
postCode varchar(50),
country varchar(60),
homePhone varchar(30),
extension float,
photo text,
notes varchar(500),
reportsTo varchar(20),
photoPath varchar(140));
\copy employees FROM 'C:\Users\mahas\Desktop\spiced_projects\week5\northwind_data_clean\data\employees.csv' DELIMITER ',' CSV HEADER;

DROP TABLE if exists order_details;
CREATE TABLE order_details
(orderId float,
productId float,
unitPrice float,
quantity float,
discount float);
\copy order_details FROM 'C:\Users\mahas\Desktop\spiced_projects\week5\northwind_data_clean\data\order_details.csv' DELIMITER ',' CSV HEADER;

DROP TABLE if exists orders;
CREATE TABLE orders
(orderId float primary key,
customerId varchar(140),
employeeId float,
orderDate date,
requiredDate date,
shippedDate varchar(100) not null,
shipVia int,
freight float,
shipName varchar(70),
shipAddress varchar(140),
shipCity varchar(140),
shipRegion varchar(30),
shipPostalCode varchar(50),
shipCountry varchar(50));
\copy orders FROM 'C:\Users\mahas\Desktop\spiced_projects\week5\northwind_data_clean\data\orders.csv' DELIMITER ',' CSV HEADER;

DROP TABLE if exists products;
CREATE TABLE products
(productId float primary key,
productName varchar(140),
supplierId int,
categoryId float,
quantityPerUnit varchar(140),
unitPrice float,
unitsInStock float,
unitsOnOrder float,
reorderLevel float,
discontinued float);
\copy products FROM 'C:\Users\mahas\Desktop\spiced_projects\week5\northwind_data_clean\data\products.csv' DELIMITER ',' CSV HEADER;

DROP TABLE if exists regions;
CREATE TABLE regions
(regionId int primary key,
regionDescription varchar(10));
\copy regions FROM 'C:\Users\mahas\Desktop\spiced_projects\week5\northwind_data_clean\data\regions.csv' DELIMITER ',' CSV HEADER;

DROP TABLE if exists shippers;
CREATE TABLE shippers
(shipperId int primary key,
companyName varchar(30),
phone varchar(30));
\copy shippers FROM 'C:\Users\mahas\Desktop\spiced_projects\week5\northwind_data_clean\data\shippers.csv' DELIMITER ',' CSV HEADER;

DROP TABLE if exists suppliers;
CREATE TABLE suppliers
(supplierId float primary key,
companyName varchar(50),
contactName varchar(50),
contactTitle varchar(50),
address varchar(140),
city varchar(50),
region varchar(50),
postalCode varchar(140),
country varchar(50),
countryCode varchar(10),
phone varchar(50),
fax varchar(50),
homePage varchar(140));
\copy suppliers FROM 'C:\Users\mahas\Desktop\spiced_projects\week5\northwind_data_clean\data\suppliers.csv' DELIMITER ',' CSV HEADER;

DROP TABLE if exists territories;
CREATE TABLE territories
(territoryId float primary key,
territoryDescription varchar(140),
regionId int);
\copy territories FROM 'C:\Users\mahas\Desktop\spiced_projects\week5\northwind_data_clean\data\territories.csv' DELIMITER ',' CSV HEADER;
