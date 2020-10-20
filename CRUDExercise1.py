from database import DatabaseContextManager


def create_table_customers():
    query = """CREATE TABLE IF NOT EXISTS Customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    company_id INTEGER,
    FOREIGN KEY (company_id) REFERENCES Companies(company_id))"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_table_companies():
    query = """CREATE TABLE IF NOT EXISTS Companies(
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    employee_count INTEGER)"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


# Create function


def create_customer(first_name: str, last_name: str, age: int, company_id: int):
    query = """INSERT INTO Customers(first_name, last_name, age, company_id) VALUES(?,?,?,?)"""
    # Question marks are used in initial query to have placeholders for upcoming parameters.
    # (This is used to protect ourselves from SQL Injection attacks)
    parameters = [first_name, last_name, age, company_id]
    # Parameters are used to pass values that were given when calling the function.
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)
        # We can pass sql and parameters to execute method which will set our values by order from parameters array or touple


def create_companies(company_name: str, employee_count: int):
    query = """INSERT INTO Companies(company_name, employee_count) VALUES(?,?)"""
    parameters = [company_name, employee_count]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


# Read function
def get_customers():
    query = """SELECT * FROM Customers"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")
    # print for convenience in terminal


def get_companies():
    query = """SELECT * FROM Companies"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")


# Update function
def update_customer_first_name(old_first_name: str, new_first_name: str):
    query = """UPDATE Customers
             SET first_name = ?
             WHERE first_name = ?"""
    parameters = [new_first_name, old_first_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def update_company_name(old_company_name: str, new_company_name: str):
    query = """UPDATE Companies
                SET company_name = ?
                WHERE company_name = ?"""
    parameters = [new_company_name, old_company_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


# Delete function
def delete_customer(first_name: str):
    query = """DELETE FROM Customers
                 WHERE first_name = ?"""
    parameters = [first_name]

    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def delete_company(company_name: str):
    query = """DELETE FROM Companies
                WHERE company_name = ?"""
    parameters = [company_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_customers_companies():
    query = """SELECT * FROM Customers
                NATURAL JOIN Companies"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)
        print("------------------------------------------------------")


def drop_table_companies():
    query = """DROP TABLE Companies"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def drop_table_customers():
    query = """DROP TABLE Customers"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


get_customers()
get_companies()
get_customers_companies()