import os
from mysql.connector import Error
from db_connection import get_db_connection, env_path

print(f"env_path is {env_path}")

connection = None
try:
    # user/password/database are read from the .env file (environment variables)
    connection = get_db_connection()
    if connection.is_connected():
        print(f"Connected successfully to database '{connection.database}' "
              f"on {connection.server_host} as user '{os.environ['DB_USERNAME']}' "
              f"(credentials loaded from environment variables)")
except Error as e:
    print(f"Error: {e}")
finally:
    if connection and connection.is_connected():
        connection.close()
        print("Database connection closed")
