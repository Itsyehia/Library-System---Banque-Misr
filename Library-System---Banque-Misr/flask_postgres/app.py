import json
import shutil
import os
from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a strong random string

# Path to the data file
DATA_FILE = '/app/data/data.json'

# Load the initial data from the JSON file
def load_initial_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Read data from the JSON file
def read_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Write data back to the JSON file
def write_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Fetch all books from the data
def get_books():
    data = read_data()
    return data['books']

# Borrow a book by updating its borrowed status
def borrow_book(book_name, user_id):
    data = read_data()
    for book in data['books']:
        if book['name'] == book_name and book['borrowedby'] is None:
            book['borrowedby'] = user_id
            write_data(data)
            return "Book borrowed successfully", "alert-success"
    return "Book not available", "alert-danger"

# Return a borrowed book
def return_book_to_library(book_name, user_id):
    data = read_data()
    for book in data['books']:
        if book['name'] == book_name and book['borrowedby'] == user_id:
            book['borrowedby'] = None
            write_data(data)
            return "Book returned successfully", "alert-success"
    return "Error returning book", "alert-danger"

# Search for books by name
def Search_books(book_name):
    data = read_data()
    return [book for book in data['books'] if book_name.lower() in book['name'].lower()]

# Create a new user in the system
def create_user(username, email, password, isAdmin):
    data = read_data()
    user_id = max(user['id'] for user in data['users']) + 1 if data['users'] else 1
    data['users'].append({"id": user_id, "username": username, "email": email, "password": password, "isAdmin": isAdmin})
    write_data(data)
    return "User created successfully", "alert-success", user_id

# Create a new admin user
def create_adminuser(username, email, password):
    data = read_data()
    user_id = max(user['id'] for user in data['admins']) + 1 if data['admins'] else 1
    data['admins'].append({"id": user_id, "username": username, "email": email, "password": password})
    write_data(data)
    return "Admin created successfully", "alert-success", user_id, 'admin'

# Validate user credentials
def check_user(email, password):
    data = read_data()
    for user in data['users'] + data['admins']:
        if user['email'] == email and user['password'] == password:
            return 'admin' if 'admins' in data and user in data['admins'] else 'user', user['id'], user.get('isAdmin', 0)
    return None, None, None

# Landing page
@app.route('/landing')
def landing():
    session.pop('user_id', None)  # Remove the user_id from the session
    return render_template('landing.html')

# Home page
@app.route('/')
def home():
    user_id = session.get('user_id')  # Retrieve user_id from the session
    if not user_id:
        return redirect(url_for('landing'))  # Redirect if user_id is not in session
    return render_template('home.html', user_id=user_id)

# Admin dashboard
@app.route('/admin/dashboard')
def admin_dashboard():
    if session.get('user_type') != 'admin':
        return redirect(url_for('home'))  # Restrict access to admin users only
    data = read_data()
    books = data['books']
    users = data['users'] + data['admins']  # Combine users and admins for admin view
    return render_template("adminDashboard.html", books=books, users=users)

# User signup
@app.route('/signupUser', methods=['GET', 'POST'])
def signupUser():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        isAdmin = 0
        message, message_class, user_id = create_user(username, email, password, isAdmin)
        if message_class == "alert-success":
            session['user_id'] = user_id
            return redirect(url_for('home'))
        else:
            return render_template('signup.html', message=message, message_class=message_class)
    return render_template('signup.html')

# Admin signup
@app.route('/admin/signup', methods=['GET', 'POST'])
def adminsignup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        message, message_class, user_id, user_type = create_adminuser(username, email, password)
        if message_class == "alert-success":
            session['user_id'] = user_id
            session['user_type'] = user_type
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template('signup.html', message=message, message_class=message_class)
    return render_template('signup.html')

# Borrow book
@app.route('/borrow', methods=['GET', 'POST'])
def borrow():
    message = None
    user_id = session.get('user_id')  # Get user_id from the session
    if not user_id:
        return redirect(url_for('signupUser'))  # Redirect to sign up if user_id is not in session
    if request.method == 'POST':
        book_name = request.form.get('book_name')
        message = borrow_book(book_name, user_id)
    books = get_books()  # Fetch the list of books from the JSON file
    return render_template('borrow.html', books=books, message=message)

# Return book
@app.route('/return', methods=['GET', 'POST'])
def return_book():
    message = None
    user_id = session.get('user_id')  # Get user_id from the session
    if not user_id:
        return redirect(url_for('signupUser'))  # Redirect to sign up if user_id is not in session
    books = [book['name'] for book in get_books() if book['borrowedby'] == user_id]  # Extract book titles
    if request.method == 'POST':
        book_name = request.form.get('book_name')
        message = return_book_to_library(book_name, user_id)
        books = [book['name'] for book in get_books() if book['borrowedby'] == user_id]
    return render_template('return.html', books=books, message=message)

# Search for books
@app.route('/searchbooks', methods=['GET', 'POST'])
def search_books():
    message = None
    books = []  # Initialize the 'books' variable with an empty list
    if request.method == 'POST':
        book_name = request.form.get('book_name')
        if not book_name:
            message = "Please enter a book name to search."
        else:
            books = Search_books(book_name) or []  # Ensure books is a list
            if not books:
                message = "No books found."
    return render_template('SearchBook.html', books=books, message=message)

# Display all books
@app.route('/ShowBooks')
def show_books():
    data = read_data()
    books = data['books']
    return render_template('ShowBooks.html', data=books)

# Add a new book
@app.route('/AddBook', methods=['GET', 'POST'])
def addbook():
    if request.method == 'POST':
        name = request.form['name']
        userID = None  # userID will be None, meaning NULL in JSON
        data = read_data()
        book_id = max(book['id'] for book in data['books']) + 1 if data['books'] else 1
        data['books'].append({'id': book_id, 'name': name, 'borrowedby': userID})
        write_data(data)
        return redirect(url_for('show_books'))  # Redirect to show books
    return render_template('Addbook.html')

# Remove a book
@app.route('/removebook/<int:book_id>', methods=['POST'])
def remove_book(book_id):
    data = read_data()
    data['books'] = [book for book in data['books'] if book['id'] != book_id]
    write_data(data)
    return redirect(url_for('show_books'))

# User login
@app.route('/loginUser', methods=['GET', 'POST'])
def loginUser():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_type, user_id, isAdmin = check_user(email, password)
        if isAdmin == 1:
            session['user_id'] = user_id
            session['user_type'] = user_type
            return redirect(url_for('admin_dashboard'))
        elif isAdmin == 0:
            session['user_id'] = user_id
            session['user_type'] = user_type
            return redirect(url_for('home'))
        else:
            return render_template('login.html', message="Invalid email or password", message_class="alert-danger")
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
