import json
import bcrypt

# Path to the JSON data file
DATA_FILE = '/app/data/data.json'

# Function to read data from the JSON file
def read_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Function to write data to the JSON file
def write_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Function to get a list of all book names from the JSON file
def get_books():
    """
    Fetches all book names from the JSON file.
    Returns a list of book names.
    """
    data = read_data()
    return [book['name'] for book in data['books']]

# Function to allow a user to borrow a book
def borrow_book(book_title, user_id):
    """
    Allows a user to borrow a book by updating its borrowedby field in the JSON file.
    Returns a message indicating the result of the operation.
    """
    data = read_data()  # Read current data
    # Search for the book by title
    for book in data['books']:
        if book['name'] == book_title:
            # If the book is available, assign it to the user
            if book['borrowedby'] is None:
                book['borrowedby'] = user_id
                write_data(data)  # Save the updated data
                return f"Book '{book_title}' has been borrowed successfully by user with ID {user_id}."
            else:
                return f"The book '{book_title}' is already borrowed."
    return f"The book '{book_title}' does not exist."

# Function to allow a user to return a book
def return_book_to_library(book_name, user_id):
    """
    Allows a user to return a borrowed book by updating its borrowedby field to None in the JSON file.
    Returns a message indicating the result of the operation.
    """
    data = read_data()  # Read current data
    # Search for the book by title
    for book in data['books']:
        if book['name'] == book_name:
            # If the book was borrowed by the user, allow the return
            if book['borrowedby'] == user_id:
                book['borrowedby'] = None
                write_data(data)  # Save the updated data
                return f"Book '{book_name}' has been returned successfully by user with ID {user_id}."
            else:
                return f"The book '{book_name}' was not borrowed by user with ID {user_id}."
    return f"The book '{book_name}' does not exist."

# Function to search for books by name (case-insensitive)
def search_books(name):
    """
    Searches for books containing the specified name in the JSON file.
    Returns a list of matching book names.
    """
    data = read_data()  # Read current data
    # Return a list of books that contain the search term in their name
    return [book['name'] for book in data['books'] if name.lower() in book['name'].lower()]

# Function to create a new user
def create_user(username, email, password, is_admin):
    """
    Creates a new user and stores them in the JSON file.
    Returns a message indicating the result of the operation.
    """
    data = read_data()  # Read current data
    # Generate a new user ID by incrementing the highest existing ID
    user_id = max(user['id'] for user in data['users']) + 1 if data['users'] else 1
    # Hash the user's password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Check if the username or email already exists
    if any(user['username'] == username for user in data['users']):
        return "Username already exists.", "alert-danger", None
    if any(user['email'] == email for user in data['users']):
        return "Email already exists.", "alert-danger", None

    # Add the new user to the list of users
    data['users'].append({"id": user_id, "username": username, "email": email, "password": hashed_password, "isAdmin": is_admin})
    write_data(data)  # Save the updated data
    return "User created successfully!", "alert-success", user_id

# Function to authenticate a user or admin
def check_user(email, password):
    """
    Checks user credentials against the data in the JSON file.
    Returns a tuple with the user type ('admin' or 'user'), user ID, and isAdmin status.
    """
    data = read_data()  # Read current data
    # Check if the email and password match any user
    for user in data['users']:
        if user['email'] == email and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            return 'user', user['id'], user['isAdmin']
    
    # Check if the email and password match any admin
    for admin in data['admins']:
        if admin['email'] == email and bcrypt.checkpw(password.encode('utf-8'), admin['password'].encode('utf-8')):
            return 'admin', admin['id'], 1
    
    return None, None, None  # Return None if no match is found

# Function to create a new admin user
def create_admin_user(username, email, password):
    """
    Creates a new admin user and stores them in the JSON file.
    Returns a message indicating the result of the operation.
    """
    data = read_data()  # Read current data
    # Generate a new admin ID by incrementing the highest existing ID
    user_id = max(admin['id'] for admin in data['admins']) + 1 if data['admins'] else 1
    # Hash the admin's password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Check if the username or email already exists
    if any(admin['username'] == username for admin in data['admins']):
        return "Username already exists.", "alert-danger", None
    if any(admin['email'] == email for admin in data['admins']):
        return "Email already exists.", "alert-danger", None

    # Add the new admin to the list of admins
    data['admins'].append({"id": user_id, "username": username, "email": email, "password": hashed_password})
    write_data(data)  # Save the updated data
    return "Admin user created successfully!", "alert-success", user_id
