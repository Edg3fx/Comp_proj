import mysql.connector as sql

PASSWORD = 'password'
DATABASE = 'amazon'

ACCOUNT_TABLE = """CREATE TABLE accounts (
    Username VARCHAR(10),
    Password VARCHAR(10) NOT NULL,
    First_Name VARCHAR(20),
    Last_Name VARCHAR(20),
    Email VARCHAR(20),
    Phone_No VARCHAR(10),
    PRIMARY KEY(Username)
)
"""

SHOP_TABLE = """CREATE TABLE shop (
    Prod_ID INT,
    Prod_Name VARCHAR(15) NOT NULL,
    Price INT,
    Stock INT,
    PRIMARY KEY(Prod_ID)
)
"""


def create_database():
    connection = sql.connect(
        host = 'localhost',
        user = 'root',
        password = PASSWORD
    )

    cursor = connection.cursor()

    cursor.execute(f"CREATE DATABASE {DATABASE}")
    cursor.execute(f"USE {DATABASE}")

    def create_account_table():
        try:
            cursor.execute(ACCOUNT_TABLE)
        except Exception as e:
            connection.rollback()


    def create_shop_table():
        try:
            cursor.execute(SHOP_TABLE)
        except Exception:
            connection.rollback()


    def insert_into_account():
        try:
            cursor.execute("INSERT INTO accounts VALUE ('edge', '1234', 'Abel', 'Varghese', 'edge123@gmail.com', '0554323345')")
            cursor.execute("INSERT INTO accounts VALUE ('arsh', '4567', 'Mohammed', 'Arsh', 'arsh@gmail.com', '0552451346')")
            cursor.execute("INSERT INTO accounts VALUE ('mathew', '7890', 'Mathew', 'George', 'mathew@gmail.com', '0553563238')")
            cursor.execute("INSERT INTO accounts VALUE ('jefferey', 'pass', 'Jefferey', 'Beta', 'jefferey@gmail.com', '0552111875')")
            cursor.execute("INSERT INTO accounts VALUE ('adonis', 'pass', 'Adonis', 'Sigma', 'adonis@gmail.com', '0550448503')")
            connection.commit()
        except Exception as e:
            connection.rollback()


    def insert_into_shop():
        try:
            cursor.execute("INSERT INTO shop VALUE (1, 'Apple', 12, 100)")
            cursor.execute("INSERT INTO shop VALUE (2, 'Banana', 10, 250)")
            cursor.execute("INSERT INTO shop VALUE (3, 'Orange', 20, 125)")
            cursor.execute("INSERT INTO shop VALUE (4, 'Grapes', 25, 60)")
            cursor.execute("INSERT INTO shop VALUE (5, 'Mango', 6, 300)")
            cursor.execute("INSERT INTO shop VALUE (6, 'Pineapple', 17, 75)")
            cursor.execute("INSERT INTO shop VALUE (7, 'Tomato', 13, 75)")
            cursor.execute("INSERT INTO shop VALUE (8, 'Pear', 18, 150)")
            cursor.execute("INSERT INTO shop VALUE (9, 'Lime', 4, 65)")
            cursor.execute("INSERT INTO shop VALUE (10, 'Cherry', 5, 25)")
            connection.commit()
        except Exception as e:
            connection.rollback()

    create_account_table()
    create_shop_table()
    insert_into_account()
    insert_into_shop()


try:
    connection = sql.connect(
        host = 'localhost',
        user = 'root',
        password = PASSWORD,
        database = DATABASE
    )
except Exception:
    print("| (i) Database not detected, creating new one...")
    create_database()
    print("|     Database successfully created!\n")
