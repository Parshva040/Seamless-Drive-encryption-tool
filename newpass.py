from oldpass import verify_password, check_strength
from getpass import getpass
from encryption import rsa_ed
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import secrets
from test import lock_dir, unlock_dir
import hashlib

def main():
    print("Enter Operation")
    print("1. Set up password")
    print("2. Access the drive")
    print("0. To exit")

def page1(password):
        text = password
        hash =  hashlib.sha256(text.encode()).hexdigest()
        if os.path.exists(".quick.txt"):
            with open(".quick.txt", "w") as f:
                f.write(hash)
        else:
            file = ".quick.txt" #it hides file in mac and linux
            with open(".quick.txt", "w") as f:
                f.write(hash)
            os.system(f' attrib +h "{file}"') #hides the file in windows
        
    
        key = secrets.token_bytes(32) #generating key of 32 bytes
        nonce = secrets.token_bytes(32)
        aes = AESGCM(key)
    
    
        #with open(file, "rb") as f:
        #    f.read()
        #rsa_ed.ciphertext = aes.encrypt(nonce, f.encode(), None) 
                    
        #new_file = os.rename(file, file + ".loc")

    
def page2(pw):
    text = pw
    word = hashlib.sha256(text.encode()).hexdigest()
    with open(".quick.txt", "r") as f:
        file = f.read()
        if word == file:
            print("access granted\n")
        else:
            print("Wrong password\n")
            
#def aes_ed(file, password): 
    #ciphertext = aes.encrypt(nonce, file.encode(), None) #encoding message using symmetric key
    #plaintext = aes.decrypt(nonce, ciphertext, None)
    #return key.hex(), ciphertext.hex(), plaintext.decode()
            
def user():
    while True:
        main()
        choice = input("Enter a number: ")
        if choice == "0":
            break
        
        elif choice == "1":
            while True:
                #file = input("enter file path: ")
                password = getpass("Enter password: ")
                if check_strength(password).startswith("weak"):
                    print("Please choose stronger password\n")
                else: 
                    password1 = getpass("Enter password again: ")
                    if password == password1:
                        page1(password)
                        print("password set\n")
                    else:
                        print("Password doesn't match\n")
                    break
                
        elif choice == "2":
            password = getpass("Enter password for accessing the drive: ")
            page2(password)
        
        else:
            print("Invalid choice please select from 0-2\n")
            
    
if __name__ == "__main__":
    user()