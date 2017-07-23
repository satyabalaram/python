import collections
def lenofstring():
    print "Enter the string:"
    string = raw_input();
    print len(string);
    count =0
    for char in string:
        count = count+1
    return  count

def countchar(string):
    count =0
    dic = {}
    for char in string:
        keys = dic.keys()
        if char in keys:
            dic[char] = dic[char] + 1
        else:
            dic[char] = 1  
    return dic

def test(string):
    length = len(string)
    if length < 2:
        return ' '
    else:
        return string[0:2]+string[-2:]

def test1(string):
    char = string[0]
    string = string.replace(char, '$')
    string = char + string[1:]
    return string  

def test2(str1, str2):
    str3 = str2[0:2] + str1[2:] 
    str4 = str1[0:2] + str2[2:]
    print str3+' '+str4
    
def test3 (string):
    length = len(string)
    print length
    if length < 3:
        return string
    elif string[-3:] == 'ing':
        string = string+'ly'
        return string
    else:
        string = string+'ing'
        return string

def test4(string):
    list = []
    list1 = []
    list = string.split(' ')
    for element in list:
        list1.append((len(element), element))
        
    list1.sort()
    
    return list1[-1][1]
def test5(string):
    return string[-1]+ string[1:-1]+ string[:1]

def temp(string):
    for index, char in enumerate(string):
        print 'current charecter ', char, 'position at', index

   
    
if __name__ == '__main__':
    #print lenofstring()
    #print countchar('google.com')
    #print test1('applea')
    #test2('abc', 'xyz')
    #print test3('string')
    #print test4('it has become a habbit to prolong')
    #print test5('12345')
    print temp('thequickbrownfoxjumpsoverthelazydog')
    
