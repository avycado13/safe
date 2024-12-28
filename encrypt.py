import getpass
import pyperclip
from cryptography.fernet import Fernet
from helpers import generate_key, clear
import time


# Encrypt the contents of a file using the provided key
def encrypt_file(filename, key):
    cipher_suite = Fernet(key)  # Initialize a Fernet object with the encryption key
    try:
        with open(filename, 'rb') as file:
            plaintext = file.read()  # Read the plaintext data from the file
    except FileNotFoundError:
        raise FileNotFoundError
    except PermissionError:
        raise PermissionError
    except Exception as e:
        print(f'Error reading file {filename}: {str(e)}')
        return

    try:
        encrypted_data = cipher_suite.encrypt(plaintext)  # Encrypt the plaintext data
    except Exception as e:
        print(f'Error encrypting file {filename}: {str(e)}')
        return

    try:
        with open(filename, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)  # Write the encrypted data to a new file
    except Exception as e:
        print(f'Error writing encrypted data to file {filename}: {str(e)}')
        return


# Get the password from the user
password = getpass.getpass('Enter password: ')
repeat_password = getpass.getpass('Reenter password: ')

while password != repeat_password:
    print('Passwords do not match')
    password = getpass.getpass('Enter password: ')
    repeat_password = getpass.getpass('Reenter password: ')

# Generate an encryption key from the password
key = generate_key(password)

# Specify the source file to be encrypted
source_file = input('File to encrypt: ')

# Encrypt the file using the generated key
encrypt_file(source_file, key)
# Inform the user about the successful encryption
print(f'{source_file} ENCRYPTED.')  # Print a message indicating successful encryption
clear()
print('______________THESE ARE YOUR CREDENTIALS______________')
print('YOU WILL NEED EITHER ONE OF THESE TO DECRYPT THE FILE ')
print('______________________________________________________')
print('PASSWORD: ' + password)

# Copy the password to the clipboard
pyperclip.copy(password)

for i in range(30, 0, -1):
    print(f"DETAILS WILL DISAPPEAR IN: {i} SECONDS", end="\r")
    time.sleep(1)
clear()
