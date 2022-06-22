import string

class Clean:
    
    @staticmethod
    def left_justify(word_list):
        adjust_length = len(max(word_list, key=len))
        new_list = [i.ljust(adjust_length) for i in word_list]
        return new_list

    @staticmethod
    def clean_website_list(string_list):
        return [i.split(',')[0] for i in string_list][1:]

    @staticmethod
    def clean_logins_list(string_list, website):
        return [i.split(',') for i in string_list if i.split(',')[0] == website][0]
        