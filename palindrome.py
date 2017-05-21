
string = str(raw_input("Enter a string\n"))
string1 = string[::-1]

print string
print string1

if (string == string1):
    print "palindrome\n"
else:
    print "not palindrome\n"


empty_string =''

for i in range(len(string)):
    empty_string += string[len(string)-1-i]


if (string == empty_string):
    print "palindrome\n"
else:
    print "not palindrome\n"
    



            



