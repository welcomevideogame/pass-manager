import string
import random


class Generator:

    @staticmethod
    def basic_gen(length=16):

        if length % 2 == 0:
            let_chars = int(length / 2)
            num_chars = int(let_chars)
        else:
            let_chars = int(round(length / 2))
            num_chars = int(length - let_chars)

        new_pass = ''.join(random.choices(string.ascii_letters, k=let_chars)) \
                   + ''.join(random.choices(string.digits, k=num_chars))
        new_pass = [char for char in new_pass]
        random.shuffle(new_pass)
        return ''.join(new_pass)


