import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# data = nonce + ciphertext

# nonce = data[:12]
# ciphertext = data[12:]

# plaintext = aes.decrypt(nonce, ciphertext, None)


#symmetric encryption

def aes_ed(message): 
    key = secrets.token_bytes(32) #generating key of 32 bytes
    nonce = secrets.token_bytes(32)
    aes = AESGCM(key)

    ciphertext = aes.encrypt(nonce, message.encode(), None) #encoding message using symmetric key
    plaintext = aes.decrypt(nonce, ciphertext, None)
    return key.hex(), ciphertext.hex(), plaintext.decode()

#asymmetric encryption

def rsa_ed(message):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(
                mgf = padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label = None
        )
    )
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
        mgf = padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label = None
        )  
    )
    #return ciphertext.hex(), plaintext.decode()
    
if __name__ == "__main__":
    path = ((input("enter path: ")))
    aes_ed(path)
    print(aes_ed(path))
    #print(rsa_ed("Hello, RSA"))