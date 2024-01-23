import os
from Crypto import Random
from Crypto.Cipher import AES
def encrypt():
    key = Random.get_random_bytes(16) # 16 bytes = 128 bits
    nonce = Random.get_random_bytes(12) # 12 bytes = 96 bits
    message_path = os.path.join("C:", "Obfuscate", "decrypted.txt") # get full path of target message file
    encrypted_path = os.path.join("C:", "Obfuscate", "test7.txt") # get full path of output encrypted file
    key_path = os.path.join("C:", "Obfuscate", "7key.txt") # get full path of key file
    with open(message_path, "rb") as f:
        data = f.read()
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    with open(encrypted_path, "wb") as f:
        f.write(nonce + tag + ciphertext) # concatenate nonce, tag and ciphertext
    with open(key_path, "wb") as f:
        f.write(key) # write key to a file

def decrypt():
    key_path = os.path.join("C:", "Obfuscate", "7key.txt") # get full path of key file
    encrypted_path = os.path.join("C:", "Obfuscate", "test7.txt") # get full path of encrypted file
    decrypted_path = os.path.join("C:", "Obfuscate", "decrypted.txt") # get full path of output decrypted file
    with open(key_path, "rb") as f:
        key = f.read() # read key from a file
    with open(encrypted_path, "rb") as f:
        nonce = f.read(12) # read nonce
        tag = f.read(16) # read tag
        ciphertext = f.read() # read ciphertext
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    with open(decrypted_path, "wb") as f:
        f.write(data)

        
encrypt() #change for decrypt/encrypt based on what is needed        
