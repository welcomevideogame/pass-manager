import string
import requests
import secrets

class Generator:
    csprng = secrets.SystemRandom()

    @classmethod
    def generate_password(cls, config, length=16):
        char_list = cls.get_chars(config)
        rand_bytes = secrets.token_bytes(length)
        password = [char_list[byte % len(char_list)] for byte in rand_bytes]
        cls.csprng.shuffle(password)
        return "".join(password)

    @classmethod
    def generate_true_password(cls, config, length=16):
        char_list = cls.get_chars(config)
        try:
            source = f"https://www.random.org/integers/?num={length}&min=0&max={len(char_list) - 1}&col=5&base=10&format=plain&rnd=new"
            nums = requests.get(source).text.replace("\n", "\t").split("\t")[:-1]
        except requests.exceptions.ConnectionError:
            return None
        password = [char_list[int(num)] for num in nums]
        cls.csprng.shuffle(password)
        return "".join(password)

    @staticmethod
    def get_chars(config):
        return ''.join([
        string.digits if config[1] else '',
        string.ascii_lowercase if config[2] else '',
        string.ascii_uppercase if config[3] else '',
        '!@#$%^&*' if config[4] else '', ])

