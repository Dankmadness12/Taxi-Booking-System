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

# Adding users (will skip if email already exists) <----------------------------------------
try:
    cursor.execute("INSERT OR IGNORE INTO Users (username, email, password, date_of_birth, phone_number, address) VALUES (?, ?, ?, ?, ?, ?)", 
    ('john_doe', 'john_dow@hotmail.com', 'password123', '1990-01-01', 7345503, 'San Juan'))
    connection.commit()
    print("Sample user inserted or already exists.")
except sqlite3.Error as e:
    print(f"Error inserting user: {e}")

# Adding another user <----------------------------------------
try:
    cursor.execute("INSERT OR IGNORE INTO Users (username, email, password, date_of_birth, phone_number, address) VALUES (?, ?, ?, ?, ?, ?)", 
    ('jada black', 'jblack@gmail.com', 'mybigboop23', '1992-12-09', 890458, 'San Fernando'))
    connection.commit()
    print("User inserted or already exists.")
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

#Adding a driver! <----------------------------------------
try:
    cursor.execute("INSERT OR IGNORE INTO Drivers (name, email, password, phone_number, license_number, vehicle_details) VALUES (?, ?, ?, ?, ?, ?)",
                   ('Maya Afton', 'mafton@gmail.com', 'password5', 7860826, '292736', 'Toyota Camry 2020'))
    connection.commit()
    print("Sample driver inserted or already exists.")
except sqlite3.Error as e:
    print(f"Error inserting driver: {e}")

#Adding another driver! <----------------------------------------
try:
    cursor.execute("INSERT OR IGNORE INTO Drivers (name, email, password, phone_number, license_number, vehicle_details) VALUES (?, ?, ?, ?, ?, ?)",
                   ('James Doakes', 'jdoakes@gmail.com', 'password6', 7860826, '123456', 'Honda Civic 2019'))
    connection.commit()
    print("Driver 2 inserted or already exists.")
except sqlite3.Error as e:
    print(f"Error inserting driver 2: {e}")
    
#Creating the Bookings Table <--------------------------------------------------------------
try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Bookings (
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL, 
            driver_id INTEGER NOT NULL,
            pickup_location TEXT NOT NULL,
            dropoff_location TEXT NOT NULL,
            pickup_time TEXT,
            status TEXT DEFAULT 'Pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            
            FOREIGN KEY (user_id) REFERENCES Users(user_id)
            FOREIGN KEY (driver_id) REFERENCES Drivers(driver_id)
        )
    ''')
    connection.commit()
    print('Booking Table successfully made!')
except sqlite3.Error as e:
    print (f"Error Creating Bookings Table: {e}")
    
#Creating the Admin Table <----------------------------------------------------------------
try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Admin (
            admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL, 
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    connection.commit()
    print ("Admin Table Created Successfully!")
except sqlite3.Error as e:
    print (f"Error creating the Admin Table: {e}")
    
#Adding an Admin <--------------------------------------------------------------------------------
try:
    cursor.execute("INSERT OR IGNORE INTO Admin (username, email, password) VALUES (?, ?, ?)",
                   ('ADMIN ONE', 'blakecheddar@taxibookings.com', 'admin1'))
    connection.commit()
    print("Admin One inserted or already exists.")
except sqlite3.Error as e:
    print(f"Error inserting Admin One: {e}")
    
#Creating the Bookings Display Table <-----------------------------------------------------------------
try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Bookings_Display (
            bookings_display_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            pickup_location TEXT NOT NULL,
            dropoff_location TEXT NOT NULL,
            
            FOREIGN KEY (user_id) REFERENCES Users(user_id)
        )
    ''')
    connection.commit()
    print('Bookings Display Table successfully made!')
except sqlite3.Error as e:
    print (f"Error Creating Bookings Display Table: {e}")


                   
                   
                   
                   
     
