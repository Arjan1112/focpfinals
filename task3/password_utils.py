# password_utils.py
import hashlib

PASSWORD_FILE = "passwd.txt"

def read_passwords():
    try:
        with open(PASSWORD_FILE, "r") as file:
            lines = file.readlines()

        passwords = [tuple(line.strip().split(":")) for line in lines if line.strip()]  # Exclude empty lines
        return passwords
    except FileNotFoundError:
        return []

def write_passwords(passwords):
    with open(PASSWORD_FILE, "w") as file:
        for username, real_name, encrypted_password in passwords:
            file.write(f"{username}:{real_name}:{encrypted_password}\n")

def encrypt_password(password):
    # You can use a more secure encryption method if needed
    return hashlib.md5(password.encode()).hexdigest()
