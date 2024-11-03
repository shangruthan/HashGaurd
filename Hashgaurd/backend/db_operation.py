import sqlite3
from .hash_generator import hash_username, verify_hash

def connect_to_db(db_name):
    """Connect to the specified SQLite database."""
    return sqlite3.connect(db_name)

def is_master_key_initialized():
    """Check if the master key is initialized in the users database."""
    conn = connect_to_db('database/users.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT master_key_hash FROM users WHERE website = ?', ('HashGuard',))
    result = cursor.fetchone()
    conn.close()
    
    return result is not None

def authenticate_master_key(master_key):
    """Authenticate the provided master key against the stored hash."""
    conn = connect_to_db('database/users.db')
    cursor = conn.cursor()

    cursor.execute('SELECT master_key_hash FROM users WHERE website = ?', ('HashGuard',))
    result = cursor.fetchone()
    conn.close()

    if result:
        stored_master_key_hash = result[0]
        return verify_hash(master_key, stored_master_key_hash)
    return False

def initialize_master_key(master_key: str):
    """Initialize the master key for the first time."""
    conn = connect_to_db('database/users.db')
    cursor = conn.cursor()

    cursor.execute('SELECT master_key_hash FROM users WHERE website = ?', ('HashGuard',))
    result = cursor.fetchone()
    
    if result:
        print("Master key already initialized. Use the 'Change Master Key' option to update it.")
        return
    
    # If no master key exists, proceed with initialization
    hashed_master_key = hash_username(master_key)
    cursor.execute('INSERT INTO users (website, hashed_username, master_key_hash) VALUES (?, ?, ?)', 
                   ('HashGuard', 'MasterUser', hashed_master_key))
    conn.commit()
    conn.close()
    print("Master key initialized!")

def change_master_key(new_master_key):
    """Change the master key to a new value."""
    conn = connect_to_db('database/users.db')
    cursor = conn.cursor()

    hashed_master_key = hash_username(new_master_key)
    cursor.execute('UPDATE users SET master_key_hash = ? WHERE website = ?', (hashed_master_key, 'HashGuard'))
    
    conn.commit()
    conn.close()
    print("Master key updated!")

def add_new_profile(website, username, password):
    """Add a new profile with the given website, username, and password."""
    conn = connect_to_db('database/users.db')
    cursor = conn.cursor()

    # Check if the master key is initialized
    cursor.execute('SELECT master_key_hash FROM users WHERE website = ?', ('HashGuard',))
    result = cursor.fetchone()

    if not result:
        print("Master key is not initialized. Please initialize the master key first.")
        conn.close()
        return

    hashed_username = hash_username(username)

    # Inserting new entry into users table
    cursor.execute('INSERT INTO users (website, hashed_username, master_key_hash) VALUES (?, ?, ?)', 
                   (website, hashed_username, result[0]))  # Use existing master key hash
    
    # Inserting into passwords table
    cursor.execute('INSERT INTO passwords (hashed_username, password) VALUES (?, ?)',
                   (hashed_username, password))

    conn.commit()
    conn.close()
    print("New profile added!")

def retrieve_password(username):
    """Retrieve the plain password associated with the entered username."""
    conn = connect_to_db('database/passwords.db')
    cursor = conn.cursor()
    
    # Hash the entered username
    hashed_username = hash_username(username)
    print(f"Hashed input username: {hashed_username}")

    # Retrieve all hashed usernames and their corresponding passwords from the database
    cursor.execute('SELECT hashed_username, password FROM passwords')
    rows = cursor.fetchall()
    conn.close()

    # Check each hashed username against the hashed username we just created
    for row in rows:
        db_hashed_username, password = row
        print(f"Comparing with database hashed username: {db_hashed_username}")

        # Verify the hash
        if verify_hash(username, db_hashed_username):
            print(f"Password found: {password}")
            return password  # Return the plain password if it matches

    print("Username does not exist.")
    return None


def update_password(username, new_password):
    """Update the password for the specified username."""
    conn = connect_to_db('database/passwords.db')
    cursor = conn.cursor()

    hashed_username = hash_username(username)  # Hash the username to match in the database
    cursor.execute('UPDATE passwords SET password = ? WHERE hashed_username = ?', (new_password, hashed_username))

    conn.commit()
    conn.close()
    print("Password updated!")

def print_all_websites():
    """Print all websites stored in the users database."""
    conn = connect_to_db('database/users.db')
    cursor = conn.cursor()

    cursor.execute('SELECT website FROM users')
    websites = cursor.fetchall()

    conn.close()
    for website in websites:
        print(website[0])
