import random

def compare_numbers(user_input, random_int):
    cowbull = [0,0]
    for i in range(len(random_int)):
        if(user_input[i] == random_int[i]):
            cowbull[0] +=1
        elif user_input[i] in random_int:
            cowbull[1] +=1
    return cowbull

random_int = str(random.randint(1000,9999))
print range(len(random_int))
print random_int

while True:
    user_input = str(raw_input("Enter 4 digit number"))
    print user_input
    cowbull = compare_numbers(user_input, random_int)

    print "you have " + str(cowbull[0]) + "cows and " + str(cowbull[1]) +"bulls\n"

    if(cowbull[0] == 4):
        print "you entered the correct string. Congrats!!"
        False
            
        
