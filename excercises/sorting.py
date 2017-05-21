def bubble_sort(list1):
    for passnum in range(len(list1)-1, 0, -1):
        print passnum
        for i in range(passnum):
            if list1[i] > list1[i+1]:
                temp = list1[i]
                list1[i] = list1[i+1]
                list1[i+1] = temp
            print list1

def selection_sort(list1):
    for passnum in range(len(list1)-1, 0, -1):
        maxpos =0
        for location in range(1,passnum+1):
            if list1[location] > list1[maxpos]:
                maxpos = location
        temp = list1[location]
        list1[passnum] = list1[maxpos]
        list1[maxpos]=temp
        
                         
list1 =  [14,46,43,27,57,41,45,21,70]
#bubble_sort(list1)
selection_sort(list1)
print list1
