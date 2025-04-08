from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt_file(file_path, key):
    # read file
    with open(file_path, 'rb') as file:
        plain_text = file.read()

    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encrypter = cipher.encryptor()

    cipher_text = encrypter.update(plain_text) + encrypter.finalize()
    encrypted_file_path = file_path + '.enc'

    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(iv + cipher_text)
    
    print(f"File '{file_path}' encrypted and save as '{encrypted_file_path}'")

key = b"123456789abcedfg"
encrypt_file('test.txt', key)