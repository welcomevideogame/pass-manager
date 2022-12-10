import string
import random
import requests
import secrets

class Generator:

    @staticmethod
    def generate_password(config, length=16):
        chars = ''.join([
            string.digits if config[1] else '',
            string.ascii_lowercase if config[2] else '',
            string.ascii_uppercase if config[3] else '',
            '!@#$%^&*' if config[4] else '', ])
        password = ''.join([secrets.choice(chars) for _ in range(length)])
        print(password)
        return password.encode('utf-8')


    @staticmethod
    def generate_true_password(config, length=16):
        chars = ''
        chars2 = ''
        char_list = ["!@#$%^&*", string.digits, string.ascii_lowercase, string.ascii_uppercase, ",.';-"]
        for i in range(len(config)):
            if config[i]:
                try:
                    source = f"https://www.random.org/integers/?num={length}&min=0&max={len(char_list[i])}&col=5&base=10&format=plain&rnd=new"
                    nums = requests.get(source).text.replace("\n", "\t").split("\t")[:-1]
                    random.SystemRandom().shuffle(nums)
                    for j in nums:
                        chars += char_list[i][int(j) - 1]
                except requests.exceptions.ConnectionError:
                    return None
        try:
            source = f"https://www.random.org/integers/?num={length}&min=0&max={len(chars)}&col=5&base=10&format=plain&rnd=new"
            nums = requests.get(source).text.replace("\n", "\t").split("\t")[:-1]
            random.SystemRandom().shuffle(nums)
            for i in nums:
                chars2 += chars[int(i) - 1]
        except requests.exceptions.ConnectionError:
            return None
        return chars2

