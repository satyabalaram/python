#str1 = "7777555511111111"
#str2 =  "3332222221111"
str1 = "9"
str2 =  "99"


list1 = list(str1)
list2 = list(str2)
print list1
print list2
if len(list1) > len(list2):
    temp = list2
    list2 = list1
    list1 = temp

len1 = len(list1)
len2 = len(list2)
diff = len2 - len1

for element in range(diff):
    list1.insert(0,0)

list3 = []

list4 = list1[: : -1]
list5 = list2[: : -1]

len1 = len(list4)

carry = 0
list3 = []

for index in range(len1):
    sum = int(list4[index]) + int(list5[index]) + carry
    carry = sum//10
    if sum >=10:
        sum = sum % 10
    list3.append(sum)

if carry:
    list3.append(carry)
 
#print list3
list3 = list3 [ : : -1]
print list3
