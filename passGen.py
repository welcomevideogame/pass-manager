import string
import random
import requests

class Generator:

    def generate_password(config, length=16):
        chars = ''
        char_list = ["!@#$%^&*", string.digits, string.ascii_lowercase, string.ascii_uppercase, ",.';-"]
        for i in range(len(config)):
            if config[i]:
                chars += ''.join(random.SystemRandom().choices(char_list[i], k=length))

        return ''.join(random.SystemRandom().choices(chars, k=length))

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

