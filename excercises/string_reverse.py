input_str = str(raw_input("enter a string to reverse: "))

print (input_str[::-1])

for char in range(len(input_str) -1, -1, -1):
    print input_str[char], end=''
    
    

