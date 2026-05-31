"""Write a Python program to create a database and a table using SQLite3."""   

import sqlite3

conn = sqlite3.connect("college.db")

cursor = conn.cursor()

create_table_query = """
                        CREATE TABLE IF NOT EXISTS students(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            age INTEGER,
                            grade TEXT
                        );
                    """

cursor.execute(create_table_query)

conn.commit()

conn.close()

print("Database and table created successfully!")
