import csv
from os.path import exists
from crypt import Encryption
from cleanser import Clean

class Save:

    file = None
    key = None

    @staticmethod
    def create_new(path):
        path = fr"{path}/logins.csv"
        if exists(path): return None
        with open(path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Website", "Username","Password"])
                return path

    def __init__(self, file, key):
        self.file = file
        self.key = key

    def save_login(self, website, username, password):
        Encryption.decrypt(self.file, self.key)
        with open(self.file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([website, username, password])
        Encryption.encrypt(self.file, self.key)

    def get_websites(self):
        return Clean.clean_website_list(self.grab_list())

    def get_login(self, website):
        return Clean.clean_logins_list(self.grab_list(), website)

    def grab_list(self):
        values = []
        Encryption.decrypt(self.file, self.key)
        with open(self.file, 'r') as f:
            reader = csv.reader(f, delimiter='\t')
            for _, line in enumerate(reader):
                values.append(line[0])
        Encryption.encrypt(self.file, self.key)
        return values

