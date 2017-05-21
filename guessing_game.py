import random

count = 0
guess = 0
number = random.randint(1,9)

while guess != number and guess != "exit":
    guess = int(raw_input("Enter a number between 1 and 9\n"))
    count +=1 
    if (guess == number):
        print "You guessed it right in", count, "times\n"
        break;
    elif (guess < number):
        print "you guessed it low\n"
    else:
        print "you guessed it high\n"

