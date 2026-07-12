import os
from pathlib import Path

def main():
    print("1. Encrypt the file")
    print("2. Decrypt the file")
    print("0. to exit")
    

def file_loc(file_path):
    new_file = os.rename(file_path, file_path + ".loc")
    

def file_unlock(file_path):
    p = Path(file_path.strip('"'))
    if p.suffix == ".loc":
        p.rename(p.with_suffix(""))

# if __name__ == "__main__":
    
# #     while True:
# #         main()
# #         choice = input("enter operation to perform: ")
# #         if choice == "0":
# #             break
#         elif choice == "1":
# #             file = input("enter file path: ")
# #             file_loc(file)
# #         elif choice == "2":
# #             file = input("Enter file path: ")
#             file_unlock(file)
#         else:
#             print("Invalid operation please choose from 0-2")
