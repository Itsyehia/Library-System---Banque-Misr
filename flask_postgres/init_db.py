import psycopg2

try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(database="BM Task", host="localhost", user="postgres", password="54321", port="5432")

    # Create a cursor object to interact with the database
    cur = conn.cursor()

    # Commit the changes to the database
    conn.commit()

    # Close the cursor
    cur.close()

except psycopg2.Error as e:
    print(f"An error occurred: {e}")

finally:
    # Ensure the connection is closed even if an error occurs
    if conn:
        conn.close()


def get_books():
    try:
        conn = psycopg2.connect(database="BM Task", host="localhost", user="postgres", password="54321", port="5432")
        cur = conn.cursor()
        cur.execute('''SELECT name FROM book ''')
        books = cur.fetchall()
        cur.close()
        return [book[0] for book in books]
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        if conn:
            conn.close()


def borrow_book(book_name, user_id):
    try:
        conn = psycopg2.connect(database="BM Task", host="localhost", user="postgres", password="54321", port="5432")
        cur = conn.cursor()
        cur.execute('''SELECT userID FROM book WHERE name = %s''', (book_name,))
        result = cur.fetchone()

        if result is None:
            message = f"The book '{book_name}' does not exist."
        elif result[0] is None:
            cur.execute('''UPDATE book SET userID = %s WHERE name = %s''', (user_id, book_name))
            conn.commit()
            message = f"Book '{book_name}' has been borrowed successfully by user with ID {user_id}."
        else:
            message = f"The book '{book_name}' is already borrowed. Please choose another one."
        cur.close()
        return message
    except psycopg2.Error as e:
        return f"An error occurred: {e}"
    finally:
        if conn:
            conn.close()


def return_book_to_library(book_name, user_id):
    try:
        conn = psycopg2.connect(database="BM Task", host="localhost", user="postgres", password="54321", port="5432")
        cur = conn.cursor()
        cur.execute('''SELECT userID FROM book WHERE name = %s''', (book_name,))
        result = cur.fetchone()

        if result is None:
            message = f"The book '{book_name}' does not exist."
        elif result[0] == user_id:
            cur.execute('''UPDATE book SET userID = NULL WHERE name = %s''', (book_name,))
            conn.commit()
            message = f"Book '{book_name}' has been returned successfully by user with ID {user_id}."
        else:
            message = f"The book '{book_name}' was not borrowed by user with ID {user_id}."
        cur.close()
        return message
    except psycopg2.Error as e:
        return f"An error occurred: {e}"
    finally:
        if conn:
            conn.close()

def Search_books(name):
    try:
        conn = psycopg2.connect(database="BM Task", host="localhost", user="postgres", password="54321", port="5432")
        cur = conn.cursor()
        # Use the LIKE operator with wildcards to search for books containing the search term
        cur.execute('''SELECT name FROM book WHERE name ILIKE %s''', (f'%{name}%',))
        books = cur.fetchall()
        cur.close()
        return [book[0] for book in books]
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        if conn:
            conn.close()



