from cryptography.fernet import Fernet
from os.path import exists

class Encryption:

    @staticmethod
    def generate_key(path):
        path = fr"{path}/key.key"
        if exists(path): return None
        key = Fernet.generate_key()
        with open(path, 'wb') as file:
            file.write(key)
            return path

    @staticmethod
    def encrypt(file, key):
        with open(key, 'rb') as filekey:
            key = filekey.read()
        fernet = Fernet(key)
        with open(file, 'rb') as f:
            orig = f.read()
        encrypted = fernet.encrypt(orig)
        with open(file, 'wb') as enc_file:
            enc_file.write(encrypted)

    @staticmethod
    def decrypt(file, key):
        with open(key, 'rb') as filekey:
            key = filekey.read()
        fernet = Fernet(key)
        with open(file, 'rb') as enc_file:
            encrypted = enc_file.read()
        decrypted = fernet.decrypt(encrypted)
        with open(file, 'wb') as dec_file:
            dec_file.write(decrypted)