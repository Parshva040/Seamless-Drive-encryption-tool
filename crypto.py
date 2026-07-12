import hashlib

text = "hello world"
hash_object = hashlib.sha256(text.encode())
hash_digest = hash_object.hexdigest()
# print("SHA has of text is ",hash_digest)

def hash_file(file_path):
    h = hashlib.new("sha256")
    with open(file_path, "rb") as file: 
        while True:
            chunk = file.read(1024)
            if chunk == b"":
                break
        h.update(chunk)
    return h.hexdigest()

def verify_integrity(file1, file2): #taking input for two files
  hash1 = hash_file(file1) # calculating hash value of file1
  hash2 = hash_file(file2) #calculating hash value of file2
  print("\n checking integrity between ", file1, " and " , file2) #Calculating hash value
  if hash1 == hash2: #comparing hash value
     return "File is intact"
  return "file maybe modified"
  
#if __name__ == "__main__":
    #print("SHA hash of file is", hash_file(input("enter file path: ")))
    #print(verify_integrity(input("enter file path 1: "), input("\n enter file path 2: ")))
    #print(verify_integrity(input("enter file path: "), input("\n enter file path 2: ")))    