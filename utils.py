# 1st party imports
import string, random, configparser, os
import os.path
# 3rd party imports
from cryptography.fernet import Fernet

if os.path.exists('key.key'):
        key = open('key.key', 'rb').read()
        fer = Fernet(key)
else:
    print("No key.key file found!\nGenerating a new key...")
    key = Fernet.generate_key()
    
    with open('key.key', 'wb') as file:
        file.write(key)
    key = open('key.key', 'rb').read()
    fer = Fernet(key)

config = configparser.ConfigParser()
config = configparser.ConfigParser();config.read('config.ini')
chars = string.ascii_letters + string.digits + string.punctuation

class util:
    def generatePassword():
        return ''.join(random.choices(chars, k=int(config['settings']['passwordLength'])))
    
    def saveAccount(site, username, password):
            with open('accounts.txt', 'a') as f:
                if not site or not username or not password:
                    print("You haven't supplied a required argument!")
                else:
                    f.write((f"site: {site} | username: {username} | password: {password}\n"))
                    print("Successfuly added account!")
    
    def loadKey():
        return open('key.key', 'rb').read()

    def viewAccounts():
        with open('accounts.txt', 'r') as f:
            print(f"\n{f.read()}")
    
    def genKey():
        key = Fernet.generate_key()
        
        with open('key.key', 'wb') as file:
            file.write(key)
    
    def encrypt(filename, key):
        f = Fernet(key)
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)

    def decrypt(filename, key):
        f = Fernet(key)
        with open(filename, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(filename, "wb") as file:
            file.write(decrypted_data)
