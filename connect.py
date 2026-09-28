from getpass import getpass
from mysql.connector import connect, Error

connection = None

try:
    connection = connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database=input("Enter database name: ")
    )

    if connection.is_connected():
        print("Database connection successful!")

except Error as e:
    print(f"Connection Error: {e}")        

finally:
    if connection and connection.is_connected():
        connection.close()
        print("Database connection closed.")