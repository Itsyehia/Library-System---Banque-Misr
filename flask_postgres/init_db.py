import psycopg2

try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(database="BM Task", host="localhost", user="postgres", password="54321", port="54321")

    # Create a cursor object to interact with the database
    cur = conn.cursor()

    # Create the 'course' table
    cur.execute('''CREATE TABLE course (id SERIAL PRIMARY KEY, name VARCHAR(100))''')

    # Insert a test record into the 'course' table
    cur.execute('''INSERT INTO course (name) VALUES ('test')''')

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
        conn = psycopg2.connect(database="BM Task", host="localhost", user="postgres", password="54321", port="54321")
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
        conn = psycopg2.connect(database="BM Task", host="localhost", user="postgres", password="54321", port="54321")
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



