import csv
from os.path import exists

class Save:


    @staticmethod
    def create_new():
        path = "./logins.csv"
        if exists(path): return 0
        with open('logins.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Website", "Username","Password"])

    @staticmethod
    def save_password(website, username, password):
        with open('logins.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([website, username, password])