import getpass
from helpers import generate_key
from cryptography.fernet import Fernet
import hashlib

# Decrypt the contents of a file using the provided key
def decrypt_file(filename, key):
    cipher_suite = Fernet(key)  # Initialize a Fernet object with the encryption key
    with open(filename, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()  # Read the encrypted data from the file
    decrypted_data = cipher_suite.decrypt(encrypted_data)  # Decrypt the encrypted data
    return decrypted_data

# Get the password from the user
password = getpass.getpass('Enter password: ')

# Generate an encryption key from the password
key = generate_key(password)

# Specify the encrypted file to be decrypted
encrypted_file = input('File to decrypt: ')

# Calculate the checksum of the encrypted file
checksum = hashlib.md5()
with open(encrypted_file, 'rb') as file:
    for chunk in iter(lambda: file.read(4096), b""):
        checksum.update(chunk)
stored_checksum = checksum.hexdigest()

# Decrypt the file using the generated key
decrypted_data = decrypt_file(encrypted_file, key)

# Calculate the checksum of the decrypted data
checksum = hashlib.md5(decrypted_data)
calculated_checksum = checksum.hexdigest()

# Compare the stored checksum with the calculated checksum
if stored_checksum == calculated_checksum:
    # Inform the user about the successful decryption
    print(f'{encrypted_file} decrypted.')  # Print a message indicating successful decryption
    print(decrypted_data)
else:
    print('File corruption detected.')

