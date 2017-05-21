



continue_flag = True

while (continue_flag):
    number = int(raw_input("Enter the number\n"))
    if (number % 2 ==0):
        print ("Entered number is even\n")
    else:
        print ("Entered number is odd\n")
    input_string = str(raw_input("do you want wish to continue\n"))
    input_string = str.lower(input_string)
    if (input_string == 'n'):
        continue_flag = False

