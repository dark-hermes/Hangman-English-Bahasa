import re

def no_strip(word):
    if re.search("^[a-zA-Z].*[a-zA-Z]$", word):
        return True
    else:
        return False

def level_1(word):
    return len(word) <= 5

def level_2(word):
    return len(word) > 5 and not ' ' in word

def level_3(word):
    return ' ' in word