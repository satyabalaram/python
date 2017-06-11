import random

print ('The purpose of this excersie is to enter a number of coin values that add up to a displayed target value')

print ('Enter coin values as 1-penny, 5-nickel, 10-dime and 25-quarter.')

print ('Hit retrun after the last entered conin value.')
print ('----------------')

terminate = False
empty_str =''

while not terminate:
    amount = random.randint(1, 99)
    print ('Enter coins that add up to', amount, 'cents, one per line')
    game_over = False
    total = 0

    while not game_over:
        valid_entry = False

        while not valid_entry:
            if total ==0:
                entry = str(input('Enter first coin: '))
            else:
                entry = str(input('Enter next coin: '))

            if entry in (empty_str, '1', '5', '10', '25'):
                valid_entry = True
            else:
                print ('Invalid entry')

        if entry == empty_str:
            if total == amount:
                print ('Correct')
            else:
                print('Sorry - you only entered', total, 'cents.')

            game_over = True
        else:
            total = total + int(entry)
            if total > amount:
                print ('Sorry - total amount exceeds', amount, 'Cents.')
                game_over = True

        if game_over:
            entry = input('\n Try again y/n?: ')

            if entry == 'n':
                terminate = True
print ('Thanks for playing .. good bye')








                
                

                       
