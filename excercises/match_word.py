a = 'umbrella'
b = 'aumbllre'

def match_word(a, b):
    c = ''
    for i in a:
        if i in b:
            c = c+ b[b.find(i)]
    return c


c = match_word(a,b)
print c
