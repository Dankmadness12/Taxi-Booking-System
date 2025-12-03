import sqlite3
connection = sqlite3.connect('database.db')

try:
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    print("Database connection confirmed.")
except sqlite3.Error as e:
    print(f"Database connection failed: {e}")
    
    cursor = connection.cursor()
    
    # Create Users table <----------------------------------------
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                date_of_birth DATE,
                phone_number INTEGER,
                address TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                
            )
        ''')
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

