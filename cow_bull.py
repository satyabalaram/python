import random
import random

def bull_cow(num, ask):
    bull = 0
    cow = 0
    while ask != num:
        ask_list=list(ask)
        num_list=list(num)

        for ii in range(0,3):
            print(ii)
            if ask_list[ii] in num_list:
                if ask_list[ii] == num_list[ii]:
                    bull += 1
                else:
                    cow += 1
            else:
                bull =0
                cow = 0
        print('Bull',bull)
        print('COW', cow)
        ask = str(input('please try again'))
    return 'finally you found the number {} by having {} bull and {} cow'.format(int(num), bull, cow)

ranDom=str(random.randint(1000,9999))
print(ranDom)
ask_number=str(input('enter a number between 1000 and 9999 as your guess'))
print(bull_cow(ranDom, ask_number))
