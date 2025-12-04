import sqlite3

try:
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    print("Database connection confirmed.")
except sqlite3.Error as e:
    print(f"Database connection failed: {e}")
    exit()

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

# Adding a user <----------------------------------------
try:
    cursor.execute("INSERT INTO Users (username, email, password, date_of_birth, phone_number, address) VALUES (?, ?, ?, ?, ?, ?)", 
    ('john_doe', 'john_dow@hotmail.com', 'password123', '1990-01-01', 7345503, 'San Juan'))
    connection.commit()
    print("User inserted successfully!")
except sqlite3.Error as e:
    print(f"Error inserting user: {e}")

# Adding another user <----------------------------------------
try:
    cursor.execute("INSERT INTO Users (username, email, password, date_of_birth, phone_number, address) VALUES (?, ?, ?, ?, ?, ?)", 
    ('jada black', 'jblack@gmail.com', 'mybigboop23', '1992-12-09', 890458, 'San Fernando'))
    connection.commit()
    print("User inserted successfully!")
except sqlite3.Error as e:
    print(f"Error inserting user: {e}")

#Create the Driver's Table <----------------------------------------
try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Drivers (
            driver_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            phone_number INTEGER,
            license_number TEXT NOT NULL UNIQUE,
            vehicle_details TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    connection.commit()
except sqlite3.Error as e:
    print(f"Error creating Drivers table: {e}")

try:
    cursor.execute("ALTER TABLE Drivers ADD COLUMN rating REAL DEFAULT 5.0")
    connection.commit()
except sqlite3.Error as e:
    print(f"Error altering Drivers table: {e}")

