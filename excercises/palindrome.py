
def palindrome(string_input):
    string_input1 = string_input
    string_input = string_input[::-1]
    if string_input1 == string_input:
        return True
    else:
        return False



if(palindrome('civic')):
    print 'Entered string is palindrome'
else:
    print 'Entered string is not palindrome'


def ispalindrom(string_input):
    left_pos =0
    right_pos = len(string_input) -1

    while right_pos >= left_pos:
        if not string_input[right_pos] == string_input[left_pos]:
            return False
        left_pos +=1
        right_pos -=1
    return True


if(ispalindrom('nursesrun')):
    print 'Entered string is palindrome'
else:
    print 'Entered string is not palindrome'
