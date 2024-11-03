import sqlite3 
import os

def initialize_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT NOT NULL,
            hashed_username TEXT NOT NULL,
            master_key_hash TEXT NOT NULL,
            UNIQUE(hashed_username)  -- Ensure hashed_username is unique
        )
    ''')
    
    # Create passwords table with a foreign key constraint
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hashed_username TEXT NOT NULL,
            password TEXT NOT NULL,
            FOREIGN KEY (hashed_username) REFERENCES users(hashed_username)
                ON DELETE CASCADE  -- Optional: remove passwords when user is deleted
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    
    initialize_database('database/users.db')
    initialize_database('database/passwords.db')
    print("Users database initialized.")
    print("Passwords database initialized.")
