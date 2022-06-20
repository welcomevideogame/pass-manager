import string

class Clean:
    
    def left_justify(word_list):
        adjust_length = len(max(word_list, key=len))
        new_list = [i.ljust(adjust_length) for i in word_list]
        return new_list
