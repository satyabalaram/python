print 'This program will convert a range of tempatures'

print 'Enter (F) to convert fahrenhiet to celsius'
print 'Enter (C) to convert celsius to Fahrenheit'

def getConvertto():
    selection = str(raw_input('Enter selection: '))
    while selection !='F' and selection !='C':
        selection = input('Enter selection: ')
    return selection
        
which = getConvertto()



starting_temp = int(input('Enter starting temperature to convert:'))
ending_temp = int(input('Enter ending temperature to convert:'))

def f_to_c(start, end):
    print 'Degree Farenheit \t Degree Celsius\n'
    for temp in range(start, end+1):
        celsius = (float(temp) - 32) * 5/9
        print format(temp,'4.1f'), '\t', format(celsius,'4.1f')

def c_to_f(start, end):
    print 'Degree Celsius \t Degree Farenheit\n'
    for temp in range(start, end+1):
        farenheit = (float(temp) - 32) * 9/5
        print format(temp,'4.1f'), '\t', format(farenheit,'4.1f')



if (which == 'F'):
    f_to_c(starting_temp,ending_temp)
else:
    c_to_f(starting_temp, ending_temp)
  
