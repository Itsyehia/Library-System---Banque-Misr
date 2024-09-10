# Stage 1: Set the base image
# Use an official Python runtime as a parent image
# The 'slim' version is a minimal base image that reduces size
FROM python:3.10-slim

# Stage 2: Set working directory
# Set the working directory in the container to /app
# All subsequent commands will run from this directory
WORKDIR /app

# Stage 3: Copy application files
# Copy the current directory contents (project files) into the container at /app
# This includes code, requirements, and other necessary files
COPY . /app

# Stage 4: Install dependencies
# Install the dependencies listed in the requirements.txt file
# --no-cache-dir prevents caching to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Stage 5: Create initial data file
# Create the initial data file inside the container
# Using a heredoc to directly write JSON data to /app/data.json
RUN cat <<EOF > /app/data.json
{
    "books": [
        {
            "id": 1,
            "name": "Book 1",
            "borrowedby": null
        },
        {
            "id": 2,
            "name": "Book 2",
            "borrowedby": 1
        },
        {
            "id": 3,
            "name": "Hero Baby",
            "borrowedby": null
        },
        {
            "id": 4,
            "name": "book 4",
            "borrowedby": null
        },
        {
            "id": 5,
            "name": "nmnm",
            "borrowedby": null
        }
    ],
    "users": [
        {
            "id": 1,
            "username": "user1",
            "email": "user1@example.com",
            "password": "hashedpassword",
            "isAdmin": 0
        },
        {
            "id": 2,
            "username": "yehiashaikhoun",
            "email": "yehiashaikhoun2002@gmail.com",
            "password": "yehia",
            "isAdmin": 0
        },
        {
            "id": 3,
            "username": "rawanfarouq",
            "email": "rawanfarouq576@gmail.com",
            "password": "rawan",
            "isAdmin": 0
        },
        {
            "id": 4,
            "username": "koky",
            "email": "koky12@gmail.com",
            "password": "1234",
            "isAdmin": 0
        },
        {
            "id": 5,
            "username": "kinzy",
            "email": "kinzy@gmail.com",
            "password": "54321",
            "isAdmin": 0
        }
    ],
    "admins": [
        {
            "id": 1,
            "username": "admin1",
            "email": "admin1@example.com",
            "password": "hashedpassword",
            "isAdmin": 1
        },
        {
            "id": 2,
            "username": "admin2",
            "email": "admin2@example.com",
            "password": "admin2",
            "isAdmin": 1
        }
    ]
}
EOF

# Stage 6: Expose the port
# Expose port 5000 to allow traffic to the Flask application
EXPOSE 5000

# Stage 7: Set environment variables
# Define environment variables for Flask
# FLASK_APP points to the main Flask file (app.py)
# FLASK_ENV sets the environment to 'development' for easier debugging
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Stage 8: Run the Flask application
# Command to run the Flask application when the container starts
# The '--host=0.0.0.0' option allows external access to the app from other machines
CMD ["flask", "run", "--host=0.0.0.0"]
