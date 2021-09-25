from cryptography.fernet import Fernet
import os

def decrypt(string):
    key = os.environ['encryption_key']

    f = Fernet(key)
    return f.decrypt(string).decode()