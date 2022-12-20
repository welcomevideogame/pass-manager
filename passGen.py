import string
import requests
import os

class Generator:
    csprng = os.urandom

    @classmethod
    def generate_password(cls, config, length=16):
        char_list = cls.get_chars(config)
        password = []
        while len(password) < length:
            rand_byte = cls.csprng(1)[0]
            char_index = rand_byte % len(char_list)
            char = char_list[char_index]
            password.append(char)
        return "".join(password)

    @classmethod
    def generate_true_password(cls, config, length=16):
        char_list = cls.get_chars(config)
        try:
            source = f"https://www.random.org/integers/?num={length}&min=0&max={len(char_list) - 1}&col=5&base=10&format=plain&rnd=new"
            nums = requests.get(source).text.replace("\n", "\t").split("\t")[:-1]
        except requests.exceptions.ConnectionError:
            return None

        password = []
        for i in range(length):
            rand_index = cls.csprng(1)[0] % (i + 1)
            char_list[i], char_list[rand_index] = char_list[rand_index], char_list[i]
            password.append(char_list[i])
        return "".join(password)

    @staticmethod
    def get_chars(config):
        return ''.join([
        string.digits if config[1] else '',
        string.ascii_lowercase if config[2] else '',
        string.ascii_uppercase if config[3] else '',
        '!@#$%^&*' if config[4] else '', ])

