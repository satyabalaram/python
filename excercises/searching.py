def binary_search(list_item, number):
    first = 0
    last = len(list_item) -1
    found = False
    while (first <= last and not found):
        mid = (first + last)/2
        if(number == list_item[mid]):
            found = True
        else:
            if(number < list_item[mid]):
                last = mid -1
            else:
                first = mid + 1
    return found

	
print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))

def Sequential_Search(list2, number):
    pos = 0
    found = False
    while pos < len(list2) and not found:
        if list2[pos] == number:
            found = True
        else:
            pos +=1
    return found

print(Sequential_Search([11,23,58,31,56,77,43,12,65,19],31))

def Ordered_binary_Search(list3, number):
    first =0
    last = len(list3) -1
    found = False
    while (first <= last and not found):
        mid = (first + last)/2
        if (number == list3[mid]):
            found = True
        else:
            if (number < list3[mid]):
                return binary_search(list3[:mid], number)
            else:
                return binary_search(list3[mid+1:], number)
                
    

print(Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 3))
print(Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 17))
