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

# Adding sample users (will skip if email already exists) <----------------------------------------
try:
    cursor.execute("INSERT OR IGNORE INTO Users (username, email, password, date_of_birth, phone_number, address) VALUES (?, ?, ?, ?, ?, ?)", 
    ('john_doe', 'john_dow@hotmail.com', 'password123', '1990-01-01', 7345503, 'San Juan'))
    connection.commit()
    print("Sample user inserted or already exists.")
except sqlite3.Error as e:
    print(f"Error inserting user: {e}")

# Adding another sample user <----------------------------------------
try:
    cursor.execute("INSERT OR IGNORE INTO Users (username, email, password, date_of_birth, phone_number, address) VALUES (?, ?, ?, ?, ?, ?)", 
    ('jada black', 'jblack@gmail.com', 'mybigboop23', '1992-12-09', 890458, 'San Fernando'))
    connection.commit()
    print("Sample user inserted or already exists.")
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
    # Check if rating column exists before adding it
    cursor.execute("PRAGMA table_info(Drivers)")
    columns = [row[1] for row in cursor.fetchall()]
    if "rating" not in columns:
        cursor.execute("ALTER TABLE Drivers ADD COLUMN rating REAL DEFAULT 5.0")
        connection.commit()
        print("Rating column added to Drivers table.")
    else:
        print("Rating column already exists in Drivers table.")
except sqlite3.Error as e:
    print(f"Error altering Drivers table: {e}")

#Adding a Driver to the Table <----------------------------------------
try:
    cursor.execute("INSERT OR IGNORE INTO Drivers (name, email, password, phone_number, license_number, vehicle_details) VALUES (?, ?, ?, ?, ?, ?)", 
    ('Samantha Cross', 'sammyc@gmail.com', 'safedriver99', 8940273, 124277, 'Toyota Camry 2020, Blue'))
    (connection.commit)
except sqlite3.Error as e:
    print(f"Error inserting driver: {e}")


