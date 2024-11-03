# HashGaurd
HashGuard is a secure password management system designed to store and manage user credentials safely. It employs hashing algorithms to ensure that sensitive information, such as passwords and usernames, remains confidential. The system provides functionalities for initializing a master key, adding new profiles, updating passwords, and retrieving stored passwords. This project is aimed at enhancing personal security in managing passwords across different websites.

#Features
Secure Hashing: Uses bcrypt to hash passwords and usernames, ensuring they are stored securely.
Master Key Management: Allows users to initialize and change a master key, which is used to encrypt stored credentials.
Profile Management: Enables users to add new profiles associated with different websites, securely storing their usernames and passwords.
Password Retrieval: Provides functionality to retrieve stored passwords by verifying the hashed username.
User-Friendly CLI: Features a command-line interface (CLI) for easy navigation and interaction with the system.

#Requirements
Python 3.6 or higher
SQLite3 (included with Python standard library)
bcrypt library for password hashing
Installation

#Clone the repository:

bash

git clone https://github.com/yourusername/HashGuard.git
cd HashGuard
Install required packages:

bash
pip install bcrypt

#Usage
Initialize the Master Key: Upon first running the program, you will be prompted to enter a master key to initialize the system. This master key will be used to encrypt your passwords.

Command Line Menu: The main menu offers several options:

Retrieve Password
Update Password
Add New Profile
Change Master Key
Print All Website Details
Exit

Adding New Profiles: Select the option to add a new profile, enter the website, username, and password. The username will be hashed before storage.

Retrieving Passwords: To retrieve a password, select the corresponding option and enter the username. The system will verify the hashed username against the stored hashes.

Changing the Master Key: If needed, you can change the master key to enhance security.

#Code Structure
backend/

hash_generator.py: Contains functions for hashing passwords and verifying hashes.
db_operation.py: Handles database operations including adding profiles, updating passwords, and retrieving stored credentials.
database/

users.db: Database file for storing user credentials and master key.
passwords.db: Database file for storing hashed usernames and plain passwords.
cli.py: The main entry point for the command-line interface.

#Security Considerations
The system uses bcrypt for hashing, which includes a unique salt for each password, making it resistant to rainbow table attacks.
Always ensure to use strong, unique passwords for your master key and other credentials.

#Contribution
Contributions to HashGuard are welcome! Please open an issue or submit a pull request if you would like to contribute.

