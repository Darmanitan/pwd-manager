import os
import os.path
from utils import util
from cryptography.fernet import Fernet

def main():
    while True:
        mode = input("Would you like to add an account or view your accounts?\nYou can also generate a new key by typing 'generate' or 'genkey', be careful as this may render the contents in your accounts.txt to not be decrypted\n --> ").lower()
        if mode == "q" or mode == "quit":
            break
        elif mode == 'generate' or mode == 'genkey':
            util.writeKey()
        elif mode == "view" or mode == "v":
            if os.stat('accounts.txt').st_size == 0 == False:
                print("There is nothing inside of your accounts.txt file!\n")
            else:
                util.decrypt('accounts.txt', key)
                util.viewAccounts()
                util.encrypt('accounts.txt', key)
        elif mode == "add" or mode == "a":
            site = input("Website? ").encode()
            username = input("Username? ").encode()
            gen = input("Would you like to generate a random password?\n --> ").lower()
            if gen == "y" or gen == "yes":
                password = util.generatePassword().encode()
            else:
                password = input("Password? ").encode()
            
            if os.stat('accounts.txt').st_size == 0 == False:
                util.saveAccount(site.decode('utf-8'), username.decode('utf-8'), password.decode('utf-8'))
                util.encrypt('accounts.txt', key)
            else:
                util.decrypt('accounts.txt', key)
                util.saveAccount(site, username, password)
                util.encrypt('accounts.txt', key)

if __name__ == "__main__":
    if os.path.exists('key.key'):
        key = util.loadKey()
        f = Fernet(key)
    else:
        print("No key.key file found!\nGenerating a new key...")
        util.genKey()
        key = util.loadKey()
        f = Fernet(key)
    
    if os.path.exists('accounts.txt'):
        pass
    else:
        file = open('accounts.txt', 'x')
        file.close
    main()