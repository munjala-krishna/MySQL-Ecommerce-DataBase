import database as db

# Driver code
if __name__ == "__main__":
    """
    Please enter the necessary information related to the DB at this place. 
    Please change PW and ROOT based on the configuration of your own system. 
    """
    PW = "4132@MySQL"  # IMPORTANT! Put your MySQL Terminal password here.
    ROOT = "root"
    DB = "ecommerce_record"  # This is the name of the database we will create in the next step - call it whatever
    # you like.
    LOCALHOST = "localhost"

    #Connecting with MySQL server
    #connection = db.create_server_connection(LOCALHOST, ROOT, PW)

    #Creating the schema in the DB 
    #db.create_and_switch_database(connection, DB, DB)

    #Connecting with the schema in MySQL
    connection = db.create_db_connection(LOCALHOST, ROOT, PW, DB)

    print("-------------------- E-Commerce Data Storage Solution -----------------------")
    print("\n")


    print("--------------------- Solution for Problem 2.b -----------------------------")
    #Inserting the data points into the orders table
    print("Inserting additional 5 new orders: ")
    new_orders = """
    INSERT INTO orders VALUES
    (101, 123456, 2, 300, '4', '13'),
    (102, 32678, 5, 100, '2', '14'),
    (103, 87612, 6, 200, '1', '15'),
    (104, 87623, 7, 120, '3', '6'),
    (105, 8971, 1, 0, '5', '7')
    """
    db.create_insert_query(connection, new_orders)
    #Data insertion in the orders table is completed.
    print("------------------- Solution for Problem 2.b is completed. --------------------")
    print("\n")


    print("--------------------- Solution for Problem 2.c -----------------------------")
    print("Listing all the orders: ")
    q1 = """
    SELECT * FROM orders;
    """
    orders = db.select_query(connection, q1)
    for order in orders:
        print(order)
    print("------------------- Solution for Problem 2.c is completed. --------------------")
    print("\n")


    print("--------------------- Solution for Problem 3.a -----------------------------")
    
    q2 = """
    SELECT * FROM orders
    WHERE total_value = (SELECT MAX(total_value) FROM orders);
    """
    max_order_detail = db.select_query(connection, q2)
    print("Order with Maximum value is: ")
    print(max_order_detail)

    q3 = """
    SELECT * FROM orders
    WHERE total_value = (SELECT MIN(total_value) FROM orders);
    """
    min_order_detail = db.select_query(connection, q3)
    print("Order with Minimum value is: ")
    print(min_order_detail)

    print("------------------- Solution for Problem 3.a is completed. --------------------")
    print("\n")


    print("--------------------- Solution for Problem 3.b -----------------------------")
    print("Listing the orders with value greater than the average order value of all the orders: ")
    q4 = """
    SELECT * FROM orders
    WHERE total_value > (SELECT AVG(total_value) FROM orders);
    """
    orders = db.select_query(connection, q4)
    for order in orders:
        print(order)
    print("------------------- Solution for Problem 3.b is completed. --------------------")
    print("\n")


    print("--------------------- Solution for Problem 3.c -----------------------------")
    print("Fetching Customers details along with their maximum total_value order")
    q5 = """
    SELECT o.customer_id, MAX(o.total_value) as MAX_Value, u.user_name, u.user_email
    FROM ecommerce_record.orders o
    LEFT JOIN ecommerce_record.users u ON o.customer_id = u.user_id
    GROUP BY o.customer_id;
    """
    highest_purchase_per_customer = db.select_query(connection, q5)
    sql='''
    INSERT INTO customer_leaderboard (customer_id, total_value, customer_name, customer_email)
    VALUES (%s, %s, %s, %s)
    '''
    print("Initiating the data insertion into the customer_leaderboard table: ")
    db.insert_many_records(connection, sql, highest_purchase_per_customer)
    print("Data is inserted into customer_leaderboard table")
    print("------------------- Solution for Problem 3.c is completed. --------------------")
    print("\n")