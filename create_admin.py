
# Import the required libraries.
import os
import getpass
import psycopg

from dotenv import load_dotenv
from werkzeug.security import generate_password_hash

# Load environment variables from the .env file.
load_dotenv()

# Read the PostgreSQL database URL.
database_url = os.getenv("DATABASE_URL")

# Check whether the database URL is available.
if not database_url:
    raise RuntimeError("DATABASE_URL environment variable is missing.")

# Get admin details securely.
name = input("Enter admin name: ")
email = input("Enter admin email: ")
password = getpass.getpass("Enter admin password: ")
confirm_password = getpass.getpass("Confirm admin password: ")

# Validate the entered information.
if not name or not email or not password:
    raise ValueError("All fields are required.")

if password != confirm_password:
    raise ValueError("Passwords do not match.")

# Hash the password before storing it.
hashed_password = generate_password_hash(password)

# Connect to the PostgreSQL database.
connection = psycopg.connect(database_url)

try:
    # Check whether the email already exists.
    existing_user = connection.execute(
        "SELECT id FROM users WHERE email = %s",
        (email,)
    ).fetchone()

    if existing_user:
        print("This email is already registered. Use a different email.")
    else:
        # Create a separate admin account.
        connection.execute(
            """
            INSERT INTO users (name, email, password, role)
            VALUES (%s, %s, %s, %s)
            """,
            (name, email, hashed_password, "admin")
        )

        # Save the database changes.
        connection.commit()

        print("Admin account created successfully!")

finally:
    # Close the database connection.
    connection.close()
