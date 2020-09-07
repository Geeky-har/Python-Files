# the program is to capitalize the first letter of the word
# Ex: harsh negi -> Harsh Negi

import string

def change(name):
    return string.capwords(name)

def change2(name):      # alternative method
    return name.title()

if __name__ == "__main__":
    name = input("Write Your name: ")

    # new_name = change(name)

    # print(new_name)

    new_name2 = change2(name)   # alternative method

    print(new_name2)