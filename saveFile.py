import csv
from os.path import exists

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
    def save_password(website, username, password):
        with open('logins.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([website, username, password])