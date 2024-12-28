import hashlib
import os, platform
# Generate a random encryption key


def generate_key(password):
    password_bytes = password.encode()
    salt = b'salt_'  # Add a salt for additional security
    key = hashlib.pbkdf2_hmac('sha256', password_bytes, salt, 100000)
    return key

def clear():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')