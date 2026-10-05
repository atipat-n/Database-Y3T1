import os
from mysql.connector import Error
from db_connection import get_db_connection

DB_NAME = os.environ.get("DB_DATABASE", "atipat_1348_db")

def create_database():
    connection = None
    try:
        connection = get_db_connection(with_db=False)
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print("Database created successfully")
    except Error as e:
        print(f"Database Error: {e}")
        raise
    finally:
        if connection and connection.is_connected():
            connection.close()

def create_table():
    connection = None
    try:
        connection = get_db_connection()
        create_students_table_query = """
        CREATE TABLE IF NOT EXISTS students (
            student_id INT PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            age INT,
            major VARCHAR(50),
            gpa FLOAT
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_students_table_query)
        connection.commit()
        print("Table 'students' created successfully")
    except Error as e:
        print(f"Database Error: {e}")
        raise
    finally:
        if connection and connection.is_connected():
            connection.close()

def insert_data():
    connection = None
    try:
        connection = get_db_connection()
        insert_students_query = """
        INSERT INTO students (student_id, first_name, last_name, age, major, gpa)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        students_data = [
            (5829, "Manee", "Jaidee", 20, "Computer Science", 3.8),
            (1002, "Jane", "Smith", 22, "Engineering", 3.9),
            (1003, "Mike", "Johnson", 21, "Biology", 3.7),
        ]
        with connection.cursor() as cursor:
            cursor.executemany(insert_students_query, students_data)
            inserted = cursor.rowcount
        connection.commit()
        print(f"Inserted {inserted} records successfully")
    except Error as e:
        print(f"Database Error: {e}")
        if connection:
            connection.rollback()
        raise
    finally:
        if connection and connection.is_connected():
            connection.close()

def show_all_students():
    connection = None
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM students ORDER BY student_id")
            rows = cursor.fetchall()

        print("All Students:")
        print(f"{'ID':<6}{'First Name':<14}{'Last Name':<14}{'Age':<6}{'Major':<20}{'GPA'}")
        print("-" * 70)
        for row in rows:
            print(f"{row[0]:<6}{row[1]:<14}{row[2]:<14}{row[3]:<6}{row[4]:<20}{row[5]}")
    except Error as e:
        print(f"Database Error: {e}")
        raise
    finally:
        if connection and connection.is_connected():
            connection.close()

def select_data():
    connection = None
    try:
        connection = get_db_connection()
        select_query = """
        SELECT student_id, first_name, last_name, major, gpa
        FROM students
        WHERE major = %s OR gpa > %s
        ORDER BY gpa DESC
        """
        with connection.cursor() as cursor:
            cursor.execute(select_query, ("Computer Science", 3.6))
            rows = cursor.fetchall()

        print("Students majoring in Computer Science or GPA > 3.6:")
        print(f"{'ID':<6}{'First Name':<14}{'Last Name':<14}{'Major':<20}{'GPA'}")
        print("-" * 70)
        for row in rows:
            print(f"{row[0]:<6}{row[1]:<14}{row[2]:<14}{row[3]:<20}{row[4]}")
    except Error as e:
        print(f"Database Error: {e}")
        raise
    finally:
        if connection and connection.is_connected():
            connection.close()

def update_data():
    connection = None
    try:
        connection = get_db_connection()
        update_query = "UPDATE students SET age = %s WHERE student_id = %s"
        with connection.cursor() as cursor:
            cursor.execute(update_query, (23, 1002))
            updated = cursor.rowcount
        connection.commit()
        print(f"Updated {updated} record(s) successfully")
    except Error as e:
        print(f"Database Error: {e}")
        if connection:
            connection.rollback()
        raise
    finally:
        if connection and connection.is_connected():
            connection.close()

def delete_data():
    connection = None
    try:
        connection = get_db_connection()
        delete_query = "DELETE FROM students WHERE student_id = %s"
        with connection.cursor() as cursor:
            cursor.execute(delete_query, (1003,))
            deleted = cursor.rowcount
        connection.commit()
        print(f"Deleted {deleted} record(s) successfully")
    except Error as e:
        print(f"Database Error: {e}")
        if connection:
            connection.rollback()
        raise
    finally:
        if connection and connection.is_connected():
            connection.close()

# Execute all functions
if __name__ == "__main__":

    print("Creating database...")
    create_database()

    print("\nCreating table...")
    create_table()

    print("\nInserting data...")
    insert_data()

    print("\nShowing all students after insert:")
    show_all_students()

    print("\nSelecting data with conditions...")
    select_data()

    print("\nUpdating data...")
    update_data()

    print("\nShowing all students after update:")
    show_all_students()

    print("\nDeleting data...")
    delete_data()

    print("\nShowing all students after delete:")
    show_all_students()
