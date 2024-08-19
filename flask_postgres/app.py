import psycopg2
from flask import Flask, render_template, redirect, url_for
from flask import request
from init_db import get_books, borrow_book, return_book_to_library, Search_books

app = Flask(__name__)


# Database connection function
def db_conn():
    """
    Establishes a connection to the PostgreSQL database.
    """
    conn = psycopg2.connect(database="BM Task", host="localhost", user="postgres", password="root", port="5432")
    return conn


# Route for the home page
@app.route('/')
def home():
    """
    Renders the home page.
    """
    return render_template('home.html')


# Route for borrowing a book
@app.route('/borrow', methods=['GET', 'POST'])
def borrow():
    """
    Handles the borrowing of a book. Validates user ID and book name,
    and processes the borrowing request.
    """
    message = None
    if request.method == 'POST':
        book_name = request.form.get('book_name')
        user_id = request.form.get('user_id')

        # Validate user_id
        try:
            user_id = int(user_id)
            if user_id <= 0:
                message = "Invalid User ID. Please enter a positive number."
            else:
                conn = db_conn()
                cur = conn.cursor()
                cur.execute('''SELECT userID FROM users WHERE userID = %s''', (user_id,))
                user_exists = cur.fetchone()
                cur.close()
                conn.close()

                if user_exists is None:
                    message = "User ID does not exist. Please enter a valid User ID."
                else:
                    message = borrow_book(book_name, user_id)
        except ValueError:
            message = "Invalid User ID. Please enter a valid number."

    books = get_books()  # Fetch the list of books from the database
    return render_template('borrow.html', books=books, message=message)


# Route for returning a book
@app.route('/return', methods=['GET', 'POST'])
def return_book():
    """
    Handles the return of a book. Validates user ID and book name,
    and processes the return request.
    """
    message = None
    if request.method == 'POST':
        book_name = request.form.get('book_name')
        user_id = request.form.get('user_id')

        # Validate user_id
        try:
            user_id = int(user_id)
            if user_id <= 0:
                message = "Invalid User ID. Please enter a positive number."
            else:
                conn = db_conn()
                cur = conn.cursor()
                cur.execute('''SELECT userID FROM users WHERE userID = %s''', (user_id,))
                user_exists = cur.fetchone()
                cur.close()
                conn.close()

                if user_exists is None:
                    message = "User ID does not exist. Please enter a valid User ID."
                else:
                    message = return_book_to_library(book_name, user_id)
        except ValueError:
            message = "Invalid User ID. Please enter a valid number."

    books = get_books()  # Fetch the list of books from the database
    return render_template('return.html', books=books, message=message)


# Route for searching books
@app.route('/searchbooks', methods=['GET', 'POST'])
def search_books():
    """
    Handles the search for books. Validates search query and returns
    search results.
    """
    message = None
    books = []  # Initialize the 'books' variable with an empty list

    if request.method == 'POST':
        book_name = request.form.get('book_name')
        print(f"Searching for book_name: {book_name}")  # Debugging line

        if not book_name:  # Check if book_name is empty
            message = "Please enter a book name to search."
        else:
            books = Search_books(book_name) or []  # Ensure books is a list
            print(f"Books found: {books}")  # Debugging line

            # Check if no books are found
            if not books:
                message = "No books found."

    return render_template('SearchBook.html', books=books, message=message)


# Route for showing all books
@app.route('/showbooks')
def show_books():
    """
    Retrieves and displays all books from the database.
    """
    try:
        conn = db_conn()
        cur = conn.cursor()
        cur.execute('''SELECT * FROM book''')
        data = cur.fetchall()  # Fetch all book records
        cur.close()
        conn.close()
        return render_template('ShowBooks.html', data=data)
    except Exception as e:
        print(f"Error: {e}")  # Log the error for debugging
        return "An error occurred while fetching books.", 500


# Route for adding a new book
@app.route('/addbook', methods=['GET', 'POST'])
def add_book():
    """
    Handles the addition of a new book to the database.
    """
    if request.method == 'POST':
        name = request.form['name']
        userID = None  # userID will be None, meaning NULL in SQL

        conn = db_conn()
        cur = conn.cursor()
        cur.execute('INSERT INTO book (name, userID) VALUES (%s, %s)', (name, userID))
        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for('show_books'))  # Redirect to show books

    return render_template('AddBook.html')


# Route for removing a book by its ID
@app.route('/removebook/<int:book_id>', methods=['POST'])
def remove_book(book_id):
    """
    Handles the removal of a book from the database by its ID.
    """
    try:
        conn = db_conn()
        cur = conn.cursor()
        cur.execute('DELETE FROM book WHERE bookID = %s', (book_id,))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('show_books'))  # Redirect to show books
    except Exception as e:
        print(f"Error: {e}")  # Log the error for debugging
        return "An error occurred while removing the book.", 500


# route for the admin page
@app.route('/admin/dashboard')
def admin_dashboard():
    try:
        conn = db_conn()
        cur = conn.cursor()

        # Fetch all books
        cur.execute('SELECT * FROM book')
        books = cur.fetchall()

        # Fetch all users
        cur.execute('SELECT * FROM users')
        users = cur.fetchall()

        cur.close()
        conn.close()

        return render_template("adminDashboard.html", books=books, users=users)
    except Exception as e:
        print(f"Error: {e}")  # Log the error for debugging
        return "An error occurred while fetching data.", 500
