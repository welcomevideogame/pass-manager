import csv
from os.path import exists
from crypt import Encryption

class Save:


    @staticmethod
    def create_new(path):
        path = fr"{path}/logins.csv"
        if exists(path): return None
        with open(path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Website", "Username","Password"])
                return path

    @staticmethod
    def save_login(file, key, website, username, password):
        Encryption.decrypt(file, key)
        with open(file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([website, username, password])
        Encryption.encrypt(file, key)
