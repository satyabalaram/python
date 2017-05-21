birthday_dic = {'Albert Einstein':'03/14/1879',
                'Benjamin Franklin':'01/17/1706',
                'Ada Lovelace':"12/10/1815",
                'Donald Trump': '06/14/1946',
                'Rowan Atkinson': '01/6/1955'}

print "welcome to brithday dictionary. we know the birthdays of:"
for key in birthday_dic:
        print key



user_input = raw_input("who's birthday do you want to look up?")

if user_input in birthday_dic:
       print('{}\'s birthday is {}.'.format(user_input, birthday_dic[user_input])) 
else:
      print('Sadly, we don\'t have {}\'s birthday.'.format(user_input))  

        
        
