import string
import random


class Generator:

    def generate_password(config, length=16):
        chars = ''
        char_list = ["!@#$%^&*", string.digits, string.ascii_lowercase, string.ascii_uppercase, ",.';-"]
        for i in range(len(config)):
            if config[i]:
                chars += ''.join(random.choices(char_list[i], k=length))
        return ''.join(random.choices(chars, k=length))
        




