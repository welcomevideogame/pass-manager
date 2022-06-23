import string

class Clean:
    
    @staticmethod
    def left_justify(word_list):
        adjust_length = len(max(word_list, key=len))
        new_list = [i.ljust(adjust_length) for i in word_list]
        return new_list

    @staticmethod
    def clean_website_list(string_list):
        new_list = []
        [new_list.append(i.split(',')[0]) for i in string_list if i.split(',')[0] not in new_list]
        return new_list[1:]

    @staticmethod
    def clean_logins_list(string_list, website, username):
        return [i.split(',') for i in string_list if i.split(',')[0] == website and i.split(',')[1] == username][0]
        
    @staticmethod
    def filter_existing_logins(string_list, website, username):
        return [i.split(',')[0] for i in string_list if i.split(',')[0] == website and i.split(',')[1] == username] != []

    @staticmethod
    def change_password_list(string_list, website, username, password):
        values = []
        for i in string_list:
            j = i.split(',')
            if j[0] == website and j[1] == username:
                j[2] = password
            values.append(j)
        return values

    @staticmethod
    def filter_usernames(string_list, website):
        return [i.split(',')[1] for i in string_list if i.split(',')[0] == website]
