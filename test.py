import os
from file import file_loc, file_unlock
import pathlib as pl

def main():
    print("select operation: ")
    print("1. folder lock")
    print("2. folder unlock")
    print("3. file lock")
    print("4. file unlock")
    print("0. to exit")
    
def lock_dir(path):
    with os.scandir(path) as ents:
        for e in ents:
            if e.is_dir():
                print(e.path)
                lock_dir(e.path)
            else:
                file_loc(e.path)

def unlock_dir(path):
    with os.scandir(path) as ents:
        for e in ents:
            if e.is_dir():
                unlock_dir(e.path)
            else:
                file_unlock(e.path)
            
def dir():
    while True:
        main()
        choice = input("enter number: ")
        if choice == "0":
            break
        elif choice == "1":
            path = input("Enter path: ")
            lock_dir(path)
        elif choice == "2":
            path = input("Enter path: ")
            unlock_dir(path)
        elif choice == "3":
            path = input("Enter path: ")
            file_loc(path)
        elif choice == "4":
            path = input("Enter path: ")
            file_unlock(path)
        else:
            print("Invalid choice please select from 0-2")

if __name__ == "__main__":
    dir()
    
    
    
    
#def verify(password2):
    #   salt = os.urandom(SALT_SIZE)
    #  pw =  derive_key(password2, salt)
    # if pw == password:
        #    v.list_files()
        #else:
        #   print("wrong password")
def dir_lock(self, path):
    with os.scandir(path) as ents:
        for e in ents:
            if e.is_dir():
                while os.walk(path):
                    name = os.path.basename(path).encode()
                    data = open(path, "r").read()
      
        enc_name = self.encrypt(name)
        enc_data = self.encrypt(data)

        #self.db.execute("INSERT INTO files VALUES (?,?)", (enc_name, enc_data))
        #self.db.commit()
        #print("Added")