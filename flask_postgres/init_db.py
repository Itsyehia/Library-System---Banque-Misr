import psycopg2

try:
    # Connect to the PostgreSQL database with specified parameters
    conn = psycopg2.connect(database="BM Task", host="localhost", user="postgres", password="root", port="5432")

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
        conn = psycopg2.connect(database="BM Task", host="localhost", user="postgres", password="root", port="5432")

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


def borrow_book(book_name, user_id):
    """
    Allows a user to borrow a book by updating its userID in the database.
    Returns a message indicating the result of the operation.
    """
    try:
        # Reconnect to the database
        conn = psycopg2.connect(database="BM Task", host="localhost", user="postgres", password="root", port="5432")

        # Create a cursor object
        cur = conn.cursor()

        # Check if the book exists and if it is currently borrowed
        cur.execute('''SELECT userID FROM book WHERE name = %s''', (book_name,))
        result = cur.fetchone()

        if result is None:
            # Book does not exist
            message = f"The book '{book_name}' does not exist."
        elif result[0] is None:
            # Book exists and is not currently borrowed; update the userID
            cur.execute('''UPDATE book SET userID = %s WHERE name = %s''', (user_id, book_name))
            conn.commit()
            message = f"Book '{book_name}' has been borrowed successfully by user with ID {user_id}."
        else:
            # Book is already borrowed
            message = f"The book '{book_name}' is already borrowed. Please choose another one."

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
    Allows a user to return a borrowed book by updating its userID to NULL in the database.
    Returns a message indicating the result of the operation.
    """
    try:
        # Reconnect to the database
        conn = psycopg2.connect(database="BM Task", host="localhost", user="postgres", password="root", port="5432")

        # Create a cursor object
        cur = conn.cursor()

        # Check if the book exists and if it was borrowed by the user
        cur.execute('''SELECT userID FROM book WHERE name = %s''', (book_name,))
        result = cur.fetchone()

        if result is None:
            # Book does not exist
            message = f"The book '{book_name}' does not exist."
        elif result[0] == user_id:
            # Book exists and was borrowed by the user; update the userID to NULL
            cur.execute('''UPDATE book SET userID = NULL WHERE name = %s''', (book_name,))
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
        conn = psycopg2.connect(database="BM Task", host="localhost", user="postgres", password="root", port="5432")

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
