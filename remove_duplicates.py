list1 = []

while True:
    num = raw_input("Enter a value\n")
    list1.append(num)
    if (num == 'done'):
        break


def remove_dup(list):
    y =[]
    for i in list:
        if i not in y:
            y.append(i)
    return y

print list1
unique_list = remove_dup(list1)
print unique_list

def remove_dup1(list1):
    return list(set(list1))


unique_list1 = remove_dup1(list1)
print unique_list1
