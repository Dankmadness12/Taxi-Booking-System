import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

# Check if table exists
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Users'")
table_exists = cur.fetchone()
print(f"Users table exists: {table_exists is not None}")

if table_exists:
    cur.execute("SELECT * FROM Users")
    rows = cur.fetchall()
    print(f"Total users in database: {len(rows)}")
    if rows:
        print("\nUsers:")
        for row in rows:
            print(row)
    else:
        print("No users found in the database.")
else:
    print("Users table does not exist.")

conn.close()
