from backend.db_operation import (
    is_master_key_initialized,
    authenticate_master_key,
    initialize_master_key,
    add_new_profile,
    retrieve_password,
    update_password,
    change_master_key,
    print_all_websites
)
from backend.hash_generator import hash_username, verify_hash

def main():
    print("Welcome to HashGuard!")

    # Check if the master key is initialized
    if is_master_key_initialized():
        # Prompt for master key to authenticate
        master_key = input("Enter master key to access the system: ")
        if not authenticate_master_key(master_key):
            print("Authentication failed. Access denied.")
            return
    else:
        # If not initialized, prompt to set a new master key
        master_key = input("Master key not initialized. Enter a new master key to initialize: ")
        initialize_master_key(master_key)

    # Indented to be part of the main function flow
    while True:
        print("\nMenu:")
        print("1. Retrieve Password")
        print("2. Update Password")
        print("3. Add New Profile")
        print("4. Change Master Key")
        print("5. Print All Website Details")
        print("6. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = retrieve_password(username)
            print(f"Password: {password}")
        elif choice == '2':
            username = input("Enter username: ")
            new_password = input("Enter new password: ")
            update_password(username, new_password)
            print("Password updated successfully.")
        elif choice == '3':
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_new_profile(website, username, password)
            print("Profile added successfully.")
        elif choice == '4':
            new_master_key = input("Enter new master key: ")
            change_master_key(new_master_key)
            print("Master key changed successfully.")
        elif choice == '5':
            print_all_websites()
        elif choice == '6':
            print("thanks for using HashGaurd")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
