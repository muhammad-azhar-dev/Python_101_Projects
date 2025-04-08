from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        data = encrypted_file.read()
    
    iv = data[:16]
    cipher_text = data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend)
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(cipher_text) + decryptor.finalize()
    decrypted_file_path = encrypted_file_path[:-4]
    
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    
    print(f"File '{encrypted_file_path}' decrypted and save as '{decrypted_file_path}'")

key = b"123456789abcedfg"
decrypt_file('test.txt.enc', key)