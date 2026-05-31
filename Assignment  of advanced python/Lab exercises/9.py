import sqlite3

def manage_database():
    connection = None

    try:
        connection = sqlite3.connect("my_database.db")
        cursor = connection.cursor()

        print("Database connected successfully!")

        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER
                    )
        """)

        print("Table 'users' is ready.")

        users_to_add = [
            ("Jainam", 21),
            ("Dhruvi", 25),
            ("Saniya", 23)
        ]

        cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)",users_to_add)

        connection.commit()

        print(f"{len(users_to_add)} rows inserted.")

        print("\nFetching data:")
        
        cursor.execute("SELECT * FROM users")

        for row in cursor.fetchall():
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        if connection is not None:
            connection.close()
            print("\nConnection closed.")

if __name__ == "__main__":
    manage_database()