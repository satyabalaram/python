import random


num1 = int(raw_input("Enter a number to generate a list range"))

list1 = random.sample(range(num1),5)


num2 = int(raw_input("Enter a number to generate a list range"))

list2 = random.sample(range(num2),10)


empty_list = []


for i in list1:
    for j in list2:
        if (i == j):
           empty_list.append(j)




print list1
print list2
print empty_list




