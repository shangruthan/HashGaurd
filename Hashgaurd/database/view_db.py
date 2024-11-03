import sqlite3

def view_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # View users table
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print("Users:")
    for user in users:
        print(user)

    # View passwords table
    cursor.execute('SELECT * FROM passwords')
    passwords = cursor.fetchall()
    print("\nPasswords:")
    for password in passwords:
        print(password)

    conn.close()

if __name__ == "__main__":
    view_database('database/users.db')
    view_database('database/passwords.db')
