""" Write a Python program to insert data into an SQLite3 database and fetch it. """

import sqlite3

# Connect to database (creates if it doesn't exist)
conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# Create table (if not already exists)
cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT
        )
""")

# ---------------------------
# Insert data into table
# ---------------------------
students_data = [
    ("Amit", 20, "A"),
    ("Neha", 22, "B"),
    ("Raj", 19, "A"),
]

cursor.executemany(
    "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
    students_data
)

conn.commit()

# ---------------------------
# Fetch data from table
# ---------------------------
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("Student Records:")
for row in rows:
    print(row)

# Close connection
conn.close()