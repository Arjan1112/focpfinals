# main.py
from password_utils import read_passwords, write_passwords, encrypt_password
# This is for adding the user use def functions.
def add_user():
    usernames = [user[0] for user in read_passwords()]

    new_username = input("Enter new username: ").lower()

    if new_username in usernames:
        print("Cannot add. Username already exists.")
        return

    real_name = input("Enter real name: ")
    password = input(" Enter password: ")

    encrypted_password = encrypt_password(password)
# This function reads the existing user data from the "passwd.txt"
    passwords = read_passwords()
    #This line appends a new tuple containing the information of the user being added
    passwords.append((new_username, real_name, encrypted_password))
# This function writes the modified list of user data
    write_passwords(passwords)
    print("User Created.")
# This is for user to login
def login():
    usernames = [user[0] for user in read_passwords()]

    username = input("User: ").lower()
    if username not in usernames:
        print("Access denied.")
        return

    password = input("Password: ")
    print(" Hey " + username + " How are you doing?")
    encrypted_password = encrypt_password(password)

    for user in read_passwords():
        if user[0] == username and user[2] == encrypted_password:
            print("Access granted.")
            return

    print("Access denied.")
# This is for deleting the user
def delete_user():
    usernames = [user[0] for user in read_passwords()]

    username_to_delete = input("Enter username: ").lower()

    passwords = read_passwords()
    updated_passwords = [user for user in passwords if user[0] != username_to_delete]

    if len(passwords) == len(updated_passwords):
        print("User not found.")
        return

    write_passwords(updated_passwords)
    print("User Deleted.")
# This is for changing the password
def change_password():
    usernames = [user[0] for user in read_passwords()]

    username = input("User: ").lower()

    if username not in usernames:
        print("User not found.")
        return

    current_password = input("Current Password: ")
    new_password = input("New Password: ")
    confirm_password = input("Confirm: ")

    if new_password != confirm_password:
        print("Passwords do not match.")
        return

    encrypted_current_password = encrypt_password(current_password)

    passwords = read_passwords()
    for i, user in enumerate(passwords):
        if user[0] == username and user[2] == encrypted_current_password:
            passwords[i] = (user[0], user[1], encrypt_password(new_password))
            write_passwords(passwords)
            print("Password changed.")
            return

    print("Invalid current password.")

if __name__ == "__main__":
    while True:
        print("\n1. Add User\n2. Login\n3. Delete User\n4. Change Password\n5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == "1":
            add_user()
        elif choice == "2":
            login()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            change_password()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please select Between 1-5, Thankyou !")
