import psycopg2

try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(database="banque misr", host="localhost", user="postgres", password="root", port="5432")

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
