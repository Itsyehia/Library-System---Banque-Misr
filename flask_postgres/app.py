import psycopg2
from flask import Flask, render_template, request, redirect, url_for
from init_db import get_books,borrow_book

app = Flask(__name__)

def db_conn():
    conn = psycopg2.connect(database="BM Task", host="localhost", user="postgres", password="54321", port="54321")
    return conn


@app.route('/')
def index():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM course''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html' , data= data)


@app.route('/create', methods=['POST'])
def create():
    conn = db_conn()
    cur = conn.cursor()
    name = request.form['name']

    # Corrected SQL statement with parameters
    cur.execute('''INSERT INTO course (name) VALUES (%s)''', (name,))

    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for('index'))

@app.route('/borrow', methods=['GET', 'POST'])
def borrow():
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
    
    books = get_books()
    return render_template('borrow.html', books=books, message=message)


