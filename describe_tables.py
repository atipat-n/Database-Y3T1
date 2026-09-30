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
        print(f"Connected successfully to {connection.database}")

    create_movies_table_query = """
    CREATE TABLE IF NOT EXISTS movies(
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100),
        release_year YEAR,
        genre VARCHAR(100),
        collection_in_mil INT
    )
    """

    create_reviewers_table_query = """
    CREATE TABLE IF NOT EXISTS reviewers(
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100)
    )
    """

    create_ratings_table_query = """
    CREATE TABLE IF NOT EXISTS ratings(
        movie_id INT,
        reviewer_id INT,
        rating DECIMAL(2,1),
        FOREIGN KEY(movie_id) REFERENCES movies(id),
        FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
        PRIMARY KEY(movie_id, reviewer_id)
    )
    """

    tables = [
        ("movies", create_movies_table_query),
        ("reviewers", create_reviewers_table_query),
        ("ratings", create_ratings_table_query),
    ]

    cursor = connection.cursor()

    for name, query in tables:
        cursor.execute(query)
        print(f"Table '{name}' created successfully")

    connection.commit()
    print("All tables created successfully!")

    for name, _ in tables:
        print("-" * 50)
        print(f"Describing '{name}' table structure:")
        cursor.execute(f"DESCRIBE {name}")
        for row in cursor.fetchall():
            print(row)

    cursor.close()

except Error as e:
    print(f"Error: {e}")

finally:
    if connection and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")