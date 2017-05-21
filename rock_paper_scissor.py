import sys

user1 = raw_input("what's your name")

user2 = raw_input("And your name")

user1_answer = raw_input("%s, do you want to chose rock, paper or scissors?" % user1)
user2_answer = raw_input("%s, do you want to chose rock, paper or scissors?" % user2)

def compare(u1, u2):

    if u1 == u2:
        return "It's a tie\n"
    elif u1 == 'rock':
        if u2 == 'scissors':
            return ("Rock wins!")
        else:
            return ("paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return ("scissors wins!")
        else:
            return ("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return ("paper wins!")
        else:
            return ("scissors wins!")
    else:
        return("Invalid input!")
        sys.exit()


print(compare(user1_answer, user2_answer))
