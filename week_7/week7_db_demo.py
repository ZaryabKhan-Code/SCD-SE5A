"""
Week 7 Demo: Basic SQLite usage (no Flask integration yet).
"""

import sqlite3

# Connect to (or create) a SQLite database
conn = sqlite3.connect('week7_demo.db')
cursor = conn.cursor()

# Create a sample table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    )
""")

# Insert a row
cursor.execute("""
    INSERT INTO users (username, email) VALUES (?, ?)
""", ("demo_user", "demo@example.com"))

conn.commit()

# Fetch and print
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
