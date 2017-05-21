fib = int(raw_input("Enter a number for fib series between 0 and :"))

list1 = []
for i in range (0, fib):
    if (i ==0):
        list1.append(i)
    elif(i == 1):
        list1.append(i)  
    else:
        list1.append(list1[i-2]+list1[i-1])
   

print list1
