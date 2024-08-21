import bcrypt
import psycopg2
from flask import Flask, render_template, redirect, url_for
from flask import request, session
from init_db import get_books, borrow_book, return_book_to_library, Search_books, create_user, check_user, \
    create_adminuser

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a strong random string

db_pass = "54321"

conn = psycopg2.connect(database="BM Task", host="db", user="postgres", password=db_pass, port="5432")


# Database connection function
def db_conn():
    """
    Establishes a connection to the PostgreSQL database.
    """
    conn = psycopg2.connect(database="BM Task", host="db", user="postgres", password=db_pass, port="5432")
    return conn


@app.route('/landing')
def landing():
    session.pop('user_id', None)  # Remove the user_id from the session

    return render_template('landing.html')


# Route for the home page
@app.route('/')
def home():
    user_id = session.get('user_id')  # Retrieve user_id from the session
    if not user_id:
        return redirect(url_for('landing'))  # Redirect if user_id is not in session
    return render_template('home.html', user_id=user_id)


@app.route('/signupUser', methods=['GET', 'POST'])
def signupUser():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        isAdmin = 0
        message, message_class, user_id = create_user(username, email, password, isAdmin)
        if message_class == "alert-success":
            # Store the userID in the session
            session['user_id'] = user_id
            return redirect(url_for('home'))
        else:
            return render_template('signup.html', message=message, message_class=message_class)

    return render_template('signup.html')


@app.route('/admin/signup', methods=['GET', 'POST'])
def adminsignup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        message, message_class, user_id, user_type = create_adminuser(username, email, password)
        if message_class == "alert-success":
            # Store the userID in the session
            session['user_id'] = user_id
            session['user_type'] = user_type
            return redirect(url_for('adminDashboard'))
        else:
            return render_template('signup.html', message=message, message_class=message_class)

    return render_template('signup.html')


# Route for borrowing a book
@app.route('/borrow', methods=['GET', 'POST'])
def borrow():
    """
    Handles the borrowing of a book. Uses the user ID from the session
    and processes the borrowing request.
    """
    message = None
    user_id = session.get('user_id')  # Get user_id from the session
    if not user_id:
        return redirect(url_for('signupUser'))  # Redirect to sign up if user_id is not in session

    if request.method == 'POST':
        book_name = request.form.get('book_name')

        # Borrow the book using the user_id from the session
        message = borrow_book(book_name, user_id)

    books = get_books()  # Fetch the list of books from the database
    return render_template('borrow.html', books=books, message=message)


# Route for returning a book
@app.route('/return', methods=['GET', 'POST'])
def return_book():
    """
    Handles the return of a book. Uses the user ID from the session
    and processes the return request.
    """
    message = None
    user_id = session.get('user_id')  # Get user_id from the session
    if not user_id:
        return redirect(url_for('signupUser'))  # Redirect to sign up if user_id is not in session

    conn = db_conn()
    cur = conn.cursor()

    # Fetch the list of books borrowed by the user
    cur.execute('''SELECT name FROM book WHERE borrowedby = %s''', (user_id,))
    borrowed_books = cur.fetchall()
    cur.close()
    conn.close()

    books = [book[0] for book in borrowed_books]  # Extract book titles from the query result

    if request.method == 'POST':
        book_name = request.form.get('book_name')

        # Return the book using the user_id from the session
        message = return_book_to_library(book_name, user_id)

        # Refresh the list of borrowed books after returning one
        conn = db_conn()
        cur = conn.cursor()
        cur.execute('''SELECT name FROM book WHERE borrowedby = %s''', (user_id,))
        borrowed_books = cur.fetchall()
        cur.close()
        conn.close()

        books = [book[0] for book in borrowed_books]

    if not books:
        message = "You have no books to return."

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
        if session.get('user_type') != 'admin':
            return redirect(url_for('home'))

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


@app.route('/loginUser', methods=['GET', 'POST'])
def loginUser():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user_type, user_id, isAdmin = check_user(email, password)

        print(isAdmin)
        if isAdmin == 1:
            session['user_id'] = user_id
            session['user_type'] = user_type  # Ensure consistent session key
            print(isAdmin,password)
            return redirect(url_for('admin_dashboard'))
        elif isAdmin == 0:
            session['user_id'] = user_id  # Ensure consistent session key
            session['user_type'] = user_type  # Ensure consistent session key
            print(isAdmin,password)
            return redirect(url_for('home'))
        else:
            message = 'Invalid email or password'
            message_class = 'alert-danger'
            print(isAdmin,password)
            return render_template('loginadmin.html', message=message, message_class=message_class)

    return render_template('loginadmin.html')
