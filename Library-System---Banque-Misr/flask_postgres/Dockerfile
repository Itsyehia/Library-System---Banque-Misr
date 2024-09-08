# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Create the initial data file inside the container using heredoc
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

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
