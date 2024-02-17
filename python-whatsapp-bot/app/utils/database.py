import sqlite3
import json


# initilazie DB
def initialize_database():
    conn = sqlite3.connect("whatsapp_users.db")
    cursor = conn.cursor()

    # Create a table to store WhatsApp user information
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                wa_no TEXT NOT NULL,
                wa_name TEXT,
                preferences TEXT
                image BLOB)"""
    )

    # Commit changes and close the connection
    conn.commit()
    conn.close()


# add user
def add_user(wa_no, wa_name, preferences=None):
    conn = sqlite3.connect("whatsapp_users.db")
    cursor = conn.cursor()

    # Check if user already exists
    cursor.execute("SELECT * FROM users WHERE wa_no = ?", (wa_no,))
    existing_user = cursor.fetchone()

    if existing_user:
        # User already exists, return False (not new)
        conn.close()
        return False
    else:
        # Insert a new user into the table
        cursor.execute(
            "INSERT INTO users (wa_no, wa_name, preferences) VALUES (?, ?, ?)",
            (wa_no, wa_name, json.dumps(preferences) if preferences else None),
        )
        conn.commit()
        conn.close()
        return True


# Retrieve User data
def get_user(wa_no):
    conn = sqlite3.connect("whatsapp_users.db")
    cursor = conn.cursor()

    # Retrieve user information from the table
    cursor.execute("SELECT * FROM users WHERE wa_no = ?", (wa_no,))
    user = cursor.fetchone()

    # Close the connection
    conn.close()

    if user:
        return (json.loads(user[3]) if user[3] else None,)
    else:
        return None


# Update User Preferences
def update_preferences(wa_no, preferences):
    conn = sqlite3.connect("whatsapp_users.db")
    cursor = conn.cursor()

    # Update user preferences in the table
    cursor.execute(
        "UPDATE users SET preferences = ? WHERE wa_no = ?",
        (json.dumps(preferences), wa_no),
    )

    # Commit changes and close the connection
    conn.commit()
    conn.close()


def update_image(wa_no, image):
    conn = sqlite3.connect("whatsapp_users.db")
    cursor = conn.cursor()

    with open("image.jpg", "rb") as file:
        image_data = file.read()

    cursor.execute(
        "UPDATE users SET image = ? WHERE wa_no = ?",
        (image_data, wa_no),
    )

    # Commit changes and close the connection
    conn.commit()
    conn.close()
