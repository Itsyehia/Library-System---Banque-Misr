import psycopg2
from psycopg2 import sql
import bcrypt

try:
    # Connect to the PostgreSQL database with specified parameters
    conn = psycopg2.connect(database="BM Task", host="localhost", user="postgres", password="54321", port="54321")

    # Create a cursor object to interact with the database
    cur = conn.cursor()

    # Commit any changes made during the session (not strictly necessary here, as no changes are made)
    conn.commit()

    # Close the cursor
    cur.close()

except psycopg2.Error as e:
    # Print any error that occurs during connection or cursor operations
    print(f"An error occurred: {e}")

finally:
    # Ensure the database connection is closed even if an error occurs
    if conn:
        conn.close()


def get_books():
    """
    Fetches all book names from the database.
    Returns a list of book names.
    """
    try:
        # Reconnect to the database
        conn = psycopg2.connect(database="BM Task", host="localhost", user="postgres", password="54321", port="54321")


        # Create a cursor object
        cur = conn.cursor()

        # Execute a query to select all book names
        cur.execute('''SELECT name FROM book''')

        # Fetch all results from the executed query
        books = cur.fetchall()

        # Close the cursor
        cur.close()

        # Return a list of book names
        return [book[0] for book in books]
    except psycopg2.Error as e:
        # Print any error that occurs during the query execution
        print(f"An error occurred: {e}")
        return []
    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()


def borrow_book(book_title, user_id):
    """
    Allows a user to borrow a book by updating its BorrowedBy field in the database.
    Returns a message indicating the result of the operation.
    """
    try:
        # Reconnect to the database
        conn = psycopg2.connect(database="BM Task", host="localhost", user="postgres", password="54321", port="54321")

        # Create a cursor object
        cur = conn.cursor()

        # Check if the book exists and if it is currently borrowed
        cur.execute('''SELECT BorrowedBy FROM book WHERE name = %s''', (book_title,))
        result = cur.fetchone()

        if result is None:
            # Book does not exist
            message = f"The book '{book_title}' does not exist."
        elif result[0] is None:
            # Book exists and is not currently borrowed; update the BorrowedBy field
            cur.execute('''UPDATE book SET BorrowedBy = %s WHERE name = %s''', (user_id, book_title))
            conn.commit()
            message = f"Book '{book_title}' has been borrowed successfully by user with ID {user_id}."
        else:
            # Book is already borrowed
            message = f"The book '{book_title}' is already borrowed. Please choose another one."

        # Close the cursor
        cur.close()
        return message
    except psycopg2.Error as e:
        # Return any error that occurs during the operation
        return f"An error occurred: {e}"
    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()


def return_book_to_library(book_name, user_id):
    """
    Allows a user to return a borrowed book by updating its BorrowedBy field to NULL in the database.
    Returns a message indicating the result of the operation.
    """
    try:
        # Reconnect to the database
        conn = psycopg2.connect(database="BM Task", host="localhost", user="postgres", password="54321", port="54321")

        # Create a cursor object
        cur = conn.cursor()

        # Check if the book exists and if it was borrowed by the user
        cur.execute('''SELECT borrowedby FROM book WHERE name = %s''', (book_name,))
        result = cur.fetchone()

        if result is None:
            # Book does not exist
            message = f"The book '{book_name}' does not exist."
        elif result[0] == user_id:
            # Book exists and was borrowed by the user; update the BorrowedBy to NULL
            cur.execute('''UPDATE book SET borrowedby = NULL WHERE name = %s''', (book_name,))
            conn.commit()
            message = f"Book '{book_name}' has been returned successfully by user with ID {user_id}."
        else:
            # Book was not borrowed by the user
            message = f"The book '{book_name}' was not borrowed by user with ID {user_id}."

        # Close the cursor
        cur.close()
        return message
    except psycopg2.Error as e:
        # Return any error that occurs during the operation
        return f"An error occurred: {e}"
    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()


def Search_books(name):
    """
    Searches for books containing the specified name in the database.
    Returns a list of matching book names.
    """
    try:
        # Reconnect to the database
        conn = psycopg2.connect(database="BM Task", host="localhost", user="postgres", password="54321", port="54321")

        # Create a cursor object
        cur = conn.cursor()

        # Execute a query to search for books containing the search term using the LIKE operator
        cur.execute('''SELECT name FROM book WHERE name ILIKE %s''', (f'%{name}%',))

        # Fetch all results from the executed query
        books = cur.fetchall()

        # Close the cursor
        cur.close()

        # Return a list of matching book names
        return [book[0] for book in books]
    except psycopg2.Error as e:
        # Print any error that occurs during the query execution
        print(f"An error occurred: {e}")
        return []
    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()


def create_user(username, email, password):
    try:
        conn = psycopg2.connect(database="BM Task", host="localhost", user="postgres", password="54321", port="54321")
        cur = conn.cursor()

        # Hash the password using bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Insert the new user into the users table and return the userID
        cur.execute(
            sql.SQL("INSERT INTO users (username, Email, PasswordHash) VALUES (%s, %s, %s) RETURNING UserID"),
            [username, email, hashed_password]
        )

        # Fetch the userID of the newly created user
        user_id = cur.fetchone()[0]

        conn.commit()
        return "User created successfully!", "alert-success", user_id

    except psycopg2.IntegrityError as e:
        conn.rollback()
        if 'users_username_key' in str(e):
            return "Username already exists. Please choose another one.", "alert-danger", None
        elif 'users_email_key' in str(e):
            return "Email already exists. Please choose another one.", "alert-danger", None
        else:
            return f"An error occurred: {e}", "alert-danger", None

    except psycopg2.Error as e:
        return f"An error occurred: {e}", "alert-danger", None

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()