import re

# define a function to select just word with alphabet character
def no_strip(word):
    if re.search("^[a-zA-Z].*[a-zA-Z]$", word):
        return True
    else:
        return False

# if letter length <= 5 
def level_1(word):
    return len(word) <= 5

# if letter length > 5 and not contain any whitespaces
def level_2(word):
    return len(word) > 5 and not ' ' in word

# if the word contain any whitespaces
def level_3(word):
    return ' ' in word