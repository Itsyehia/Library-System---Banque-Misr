import psycopg2
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def db_conn():
    conn = psycopg2.connect(database="banque misr", host="localhost", user="postgres", password="root", port="5432")
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
