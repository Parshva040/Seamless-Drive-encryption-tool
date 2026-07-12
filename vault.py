import os
import sqlite3
from getpass import getpass
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt




SALT_SIZE = 16
NONCE_SIZE = 12
KEY_SIZE = 32


def derive_key(password, salt):    
    kdf = Scrypt(salt=salt, length=KEY_SIZE, n=2**14, r=8, p=1)
    return kdf.derive(password.encode())



class Vault: #defines class name vault
    def __init__(self, path, password):
        self.path = path
        self.salt_path = path + ".salt"

        if not os.path.exists(self.salt_path): #checks custom partition
            salt = os.urandom(SALT_SIZE)    #create custom partition if unavailable
            open(self.salt_path, "wb").write(salt)  #Opens it
        else:
            salt = open(self.salt_path, "rb").read() #Open it partition already exists

        password = derive_key(password, salt)   #Add salt to password
        self.aes = AESGCM(password) #encrypts it
        
        self.db = sqlite3.connect(self.path)    # Creates database
        self.db.execute("""
        CREATE TABLE IF NOT EXISTS files(
            name BLOB,
            data BLOB
        )
        """)

        
    def encrypt(self, data):    # For data encryption
        nonce = os.urandom(NONCE_SIZE)
        return nonce + self.aes.encrypt(nonce, data, None)

    def decrypt(self, data):    # For data decryption
        nonce = data[:NONCE_SIZE]
        ct = data[NONCE_SIZE:]
        return self.aes.decrypt(nonce, ct, None)
    
    def dir_lock(self, path): #  scanning directory recursively
        with os.scandir(path) as ents:
            for e in ents:
                if e.is_dir():
                    while os.walk(path):
                        name = os.path.basename(path).encode()
                        data = open(path, "rb").read()
                    
        enc_name = self.encrypt(name)
        enc_data = self.encrypt(data)
        
        self.db.execute("INSERT INTO files VALUES (?,?)", (enc_name, enc_data))
        self.db.commit()
        print("Added")

    def add_file(self, filepath): #adds file to custom partition and then encrypts it
        name = os.path.basename(filepath).encode()
        data = open(filepath, "rb").read()

        enc_name = self.encrypt(name)
        enc_data = self.encrypt(data)

        self.db.execute("INSERT INTO files VALUES (?,?)", (enc_name, enc_data))
        self.db.commit()
        print("Added")

    def list_files(self):   # list files from custom partition
        rows = self.db.execute("SELECT name FROM files")
        for r in rows:
            print(self.decrypt(r[0]).decode())

    def extract_all(self):  #Extracts files from custom partition
        rows = self.db.execute("SELECT name,data FROM files")
        for name, data in rows:
            fname = self.decrypt(name).decode()
            content = self.decrypt(data)
            open(fname, "wb").write(content)
            print("Extracted", fname)


if __name__ == "__main__": #main function
    password = getpass("Vault password: ")
    v = Vault("vault.db", password)

    while True:
        cmd = input("add/list/extract/Dir/quit: ")

        if cmd == "add":
            password = input("file path: ")
            v.add_file(password)
        elif cmd == "list":
            v.list_files()
        elif cmd == "extract":
            password2 = getpass("Give password of vault: ")
            if password2 == password:
                v.extract_all()
            else:
                print("Invalid password")
        elif cmd == "dir":
            path = input("Enter path: ")
            v.dir_lock(path)
        elif cmd == "quit":
            break
        else:
            print("Invalid operation")
