from database import DatabaseContextManager


def create_table_customers():
    query = """CREATE TABLE IF NOT EXISTS Customers(
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        amount_spent INTEGER)"""
    with DatabaseContextManager("ordersdb") as ordersdb:
        ordersdb.execute(query)


def create_table_products():
    query = """CREATE TABLE IF NOT EXISTS Products(
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                price INTEGER)"""
    with DatabaseContextManager("ordersdb") as ordersdb:
        ordersdb.execute(query)


def create_table_orders():
    query = """CREATE TABLE IF NOT EXISTS Orders(
                        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_id INTEGER,
                        product_id INTEGER,
                        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
                        FOREIGN KEY (product_id) REFERENCES Products(product_id))"""
    with DatabaseContextManager("ordersdb") as ordersdb:
        ordersdb.execute(query)


# ------------------------------------------------------------------------------------------------------------#

def create_customer(first_name: str, last_name: str, amount_spent: int):
    query = """INSERT INTO Customers(first_name, last_name, amount_spent) VALUES(?,?,?)"""
    parameters = [first_name, last_name, amount_spent]
    with DatabaseContextManager("ordersdb") as ordersdb:
        ordersdb.execute(query, parameters)


def create_product(name: str, description: str, price: int):
    query = """INSERT INTO Products(name, description, price) VALUES(?,?,?)"""
    parameters = [name, description, price]
    with DatabaseContextManager("ordersdb") as ordersdb:
        ordersdb.execute(query, parameters)


def create_order(customer_id: int, product_id: int):
    query = """INSERT INTO Orders(customer_id, product_id) VALUES(?,?)"""
    parameters = [customer_id, product_id]
    with DatabaseContextManager("ordersdb") as ordersdb:
        ordersdb.execute(query, parameters)


# ------------------------------------------------------------------------------------------------------------#

def get_customers():
    query = """SELECT * FROM Customers"""
    with DatabaseContextManager("ordersdb") as ordersdb:
        ordersdb.execute(query)
        for record in ordersdb.fetchall():
            print(record)
    print("------------------------------------------------------")


def get_products():
    query = """SELECT * FROM Products"""
    with DatabaseContextManager("ordersdb") as ordersdb:
        ordersdb.execute(query)
        for record in ordersdb.fetchall():
            print(record)
    print("------------------------------------------------------")


def get_orders():
    query = """SELECT * FROM Orders"""
    with DatabaseContextManager("ordersdb") as ordersdb:
        ordersdb.execute(query)
        for record in ordersdb.fetchall():
            print(record)
    print("------------------------------------------------------")


def get_customers_products_orders():
    query = """SELECT * FROM Customers, Products
                    NATURAL JOIN Orders"""
    with DatabaseContextManager("ordersdb") as ordersdb:
        ordersdb.execute(query)
        for row in ordersdb.fetchall():
            print(row)
    print("------------------------------------------------------")


# ------------------------------------------------------------------------------------------------------------#

def update_customer_amount_spent(old_amount_spent: int, new_amount_spent: int):
    query = """UPDATE Customers
             SET amount_spent = ?
             WHERE amount_spent = ?"""
    parameters = [new_amount_spent, old_amount_spent]
    with DatabaseContextManager("ordersdb") as ordersdb:
        ordersdb.execute(query, parameters)


def update_product_price(old_price: int, new_price: int):
    query = """UPDATE Products
                     SET price = ?
                     WHERE price = ?"""
    parameters = [new_price, old_price]
    with DatabaseContextManager("ordersdb") as ordersdb:
        ordersdb.execute(query, parameters)


def update_order_id(old_order_id: int, new_order_id: int):
    query = """UPDATE Orders
                             SET first_name = ?
                             WHERE first_name = ?"""
    parameters = [new_order_id, old_order_id]
    with DatabaseContextManager("ordersdb") as ordersdb:
        ordersdb.execute(query, parameters)


# ------------------------------------------------------------------------------------------------------------#


def delete_customer(first_name: str):
    query = """DELETE FROM Customers
                WHERE first_name = ?"""
    parameters = [first_name]
    with DatabaseContextManager("ordersdb") as ordersdb:
        ordersdb.execute(query, parameters)


def delete_product(name: str):
    query = """DELETE FROM Products
                WHERE name = ?"""
    parameters = [name]
    with DatabaseContextManager("ordersdb") as ordersdb:
        ordersdb.execute(query, parameters)


def delete_order(order_id: int):
    query = """DELETE FROM Orders
                WHERE order_id = ?"""
    parameters = [order_id]
    with DatabaseContextManager("ordersdb") as ordersdb:
        ordersdb.execute(query, parameters)


# ------------------------------------------------------------------------------------------------------------#

def drop_customers_table():
    query = """DROP TABLE Customers"""
    with DatabaseContextManager("ordersdb") as ordersdb:
        ordersdb.execute(query)


def drop_products_table():
    query = """DROP TABLE Products"""
    with DatabaseContextManager("ordersdb") as ordersdb:
        ordersdb.execute(query)


def drop_orders_table():
    query = """DROP TABLE Orders"""
    with DatabaseContextManager("ordersdb") as ordersdb:
        ordersdb.execute(query)

# ------------------------------------------------------------------------------------------------------------#
