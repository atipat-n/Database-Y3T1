import os
from dotenv import load_dotenv
from mysql.connector import connect

# Load environment variables from .env file
env_path = os.path.join(os.path.dirname(__file__), ".env")
env_loaded = load_dotenv(dotenv_path=env_path, override=True)


def get_db_connection(with_db=True):
    """Create database connection with proper configuration"""
    config = {
        "host": os.environ.get("DB_HOST", "localhost"),
        "user": os.environ["DB_USERNAME"],
        "password": os.environ["DB_PASSWORD"],
        "autocommit": False,
        "charset": "utf8mb4",
    }
    if with_db:
        config["database"] = os.environ.get("DB_DATABASE", "movies_1348_db")
    return connect(**config)

# Test this module directly: python db_connection.py
if __name__ == "__main__":
    if env_loaded:
        print("Loading environment variables successfully")

    db_name = os.environ.get("DB_DATABASE", "movies_1348_db")
    print(f"Trying to connect {db_name}")

    connection = get_db_connection()
    if connection.is_connected():
        print(f"Connected to {connection.database} successfully")
        connection.close()
