import csv
import database as db

PW = "4132@MySQL"  # IMPORTANT! Put your MySQL Terminal password here.
ROOT = "root"
DB = "ecommerce_record"  # This is the name of the database we will create in the next step - call it whatever you like.
LOCALHOST = "localhost"  # considering you have installed MySQL server on your computer

RELATIVE_CONFIG_PATH = 'C:/Users/Munjala Hari Krishna/Desktop/MySQL/Assignment/C03-Project01-02-Ecommerce Data Storage/config/'

USER = 'users'
PRODUCTS = 'products'
ORDER = 'orders'

connection = db.create_server_connection(LOCALHOST, ROOT, PW)

# creating the schema in the DB
db.create_and_switch_database(connection, DB, DB)

# Create the tables through python code here
# if you have created the table in UI, then no need to define the table structure
# If you are using python to create the tables, call the relevant query to complete the creation

#Creating Users Table
create_users_table = """
     CREATE TABLE IF NOT EXISTS users (
        user_id varchar(10) PRIMARY KEY,
        user_name varchar(45) NOT NULL,
        user_email varchar(45) NOT NULL,
        user_password varchar(45) NOT NULL,
        user_address varchar(45) NULL,
        is_vendor tinyint(1) DEFAULT 0
     )
    """

#Creating Products Table
create_products_table = """
    CREATE TABLE IF NOT EXISTS products (
        product_id varchar(45) NOT NULL PRIMARY KEY,
        product_name varchar(45) NOT NULL,
        product_description varchar(100) NOT NULL,
        product_price float(45) NOT NULL,
        emi_available varchar(10) NOT NULL,
        vendor_id varchar(10) NOT NULL,
        FOREIGN KEY (vendor_id) REFERENCES users (user_id)
    )
    """

#Creating Orders Table
create_orders_table = """
    CREATE TABLE IF NOT EXISTS orders (
        order_id int PRIMARY KEY,
        total_value float(45) NOT NULL,
        order_quantity int NOT NULL,
        reward_point int NOT NULL,
        vendor_id varchar(10) NOT NULL,
        customer_id varchar(10) NOT NULL,
        FOREIGN KEY (vendor_id) REFERENCES users (user_id),
        FOREIGN KEY (customer_id) REFERENCES users (user_id)
    )
    """

#Creating Customer Leaderboard Table
create_customer_leaderboard = """
    CREATE TABLE IF NOT EXISTS customer_leaderboard (
        customer_id varchar(10) PRIMARY KEY,
        total_value float(45) NOT NULL,
        customer_name varchar(50) NOT NULL,
        customer_email varchar(50) NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES users (user_id)
    )
    """


print("--------------------- E-Commerce Data Storage Solution ------------------------")
print("\n")


print("--------------------- Solution for Problem 1.a -----------------------------")
#Connecting to MySQL Server
connection = db.create_server_connection(LOCALHOST, ROOT, PW)
#Creating the schema in DB
db.create_and_switch_database(connection, DB, DB)
print("------------------- Solution for Problem 1.a is completed. --------------------")
print("\n")


print("--------------------- Solution for Problem 1.b -----------------------------")
print("Initiating creation of Tables: ")
print("\n")
db.create_table(connection, create_users_table) #Executes our defined query
print("Users table created")
print("\n")
db.create_table(connection, create_products_table) #Executes our defined query
print("Products table created")
print("\n")
db.create_table(connection, create_orders_table) #Executes our defined query
print("Orders table created")
print("\n")
db.create_table(connection, create_customer_leaderboard) #Executes our defined query
print("Customer Leaderboard table created")
print("------------------- Solution for Problem 1.b is completed. --------------------")
print("\n")


print("--------------------- Solution for Problem 2.a -----------------------------")

print("Initiating the data insertion into Users table.")
with open(RELATIVE_CONFIG_PATH + USER + '.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))
    val.pop(0)
    sql = '''
    INSERT INTO users (user_id, user_name, user_email, user_password, user_address, is_vendor)
    VALUES (%s, %s, %s, %s, %s, %s)
    '''
    db.insert_many_records(connection, sql, val)
print("Data insertion into Users table is completed")
print("\n")

print("Initiating the data insertion into Products table.")
with open(RELATIVE_CONFIG_PATH + PRODUCTS + '.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))
    val.pop(0)
    sql = '''
    INSERT INTO products (product_id, product_name, product_price, product_description, vendor_id, emi_available)
    VALUES (%s, %s, %s, %s, %s, %s)
    '''
    db.insert_many_records(connection, sql, val)
print("Data insertion into Products table is completed")
print("\n")

print("Initiating the data insertion into Orders table.")
with open(RELATIVE_CONFIG_PATH + ORDER + '.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))

    val.pop(0)
    sql = '''
    INSERT INTO orders (order_id, customer_id, vendor_id, total_value, order_quantity, reward_point)
    VALUES (%s, %s, %s, %s, %s, %s)
    '''
    db.insert_many_records(connection, sql, val)
print("Data insertion into Orders table is completed.")

print("------------------- Solution for Problem 2.a is completed. --------------------")
