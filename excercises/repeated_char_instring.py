
def find_repeated_chars(string):
    chars = dict()
    for i in string:
        chars[i]= string.count(i)
    return chars


string = 'thequickbrownfoxjumpsoverthelazydog'

print find_repeated_chars(string)
