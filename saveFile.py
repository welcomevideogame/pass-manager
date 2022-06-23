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
        if self.check_exists(website, username): return 0
        Encryption.decrypt(self.file, self.key)
        with open(self.file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([website, username, password])
        Encryption.encrypt(self.file, self.key)
        return 1
    
    def overwrite_login(self, website, username, password):
        updated_logins = Clean.change_password_list(self.grab_list(), website, username, password)
        Encryption.decrypt(self.file, self.key)
        with open(self.file, 'w', newline='') as f:
            f.truncate()
            writer = csv.writer(f)
            for i in updated_logins:
                writer.writerow([i[0], i[1], i[2]])
        Encryption.encrypt(self.file, self.key)

    def check_exists(self, website, username):
        return Clean.filter_existing_logins(self.grab_list(), website, username)

    def get_websites(self):
        return Clean.clean_website_list(self.grab_list())

    def get_login(self, website, username):
        return Clean.clean_logins_list(self.grab_list(), website, username)

    def get_usernames(self, website):
        return Clean.filter_usernames(self.grab_list(), website)

    def grab_list(self):
        values = []
        Encryption.decrypt(self.file, self.key)
        with open(self.file, 'r') as f:
            reader = csv.reader(f, delimiter='\t')
            for _, line in enumerate(reader):
                values.append(line[0])
        Encryption.encrypt(self.file, self.key)
        return values

