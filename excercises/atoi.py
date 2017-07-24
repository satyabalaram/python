def isNumericChar(x):
    if (x >= '0' and x <= '9'):
        return True
    return False

def myAtoi(string):
    res = 0
    sign = 1
    i = 0
    if string[0] == '-':
        sign = -1
        i = i+1
    
    for i in xrange(i, len(string)):
        if isNumericChar(string[i] == False):
            return 0
        
        res = res*10 + (ord(string[i]) - ord('0'))

    return res*sign

# Driver program
string = "-134"
print myAtoi(string)
