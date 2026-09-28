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

    create_db_query = "CREATE DATABASE IF NOT EXISTS movie_db"

    cursor = connection.cursor()
    cursor.execute(create_db_query)
    print("Database created successfully!")

    cursor.close()

except Error as e:
    print(f"Error: {e}")        

finally:
    if connection and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")