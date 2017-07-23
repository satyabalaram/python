from random import shuffle
import itertools
import random
import collections

def test(list):
    count =  0
    for element in list:
        length = len(element)
        if element[0] == element[length-1]:
            count = count+1
    return count
def removedup(list, int):
    num = int
    list1 = []
    for element in list:
        if len(element) > int:
            list1.append(element)
    return list1

def common_mem(list1, list2):
    for element in list1:
        if element in list2:
            return True
    return False

def test1(list):
    list1 = []
    for element in list:
        if element % 2 == 0:
           list1.append(element)
    shuffle(list1)
    return list1
def test2():
    list =[]
    for i in range(1,31):
        if i <= 5 or i >= 25:
            list.append(i**2)
    return list

def difference(list1, list2):
    list3 = []
    list4 = []
    for element in list1:
        if element not in list2:
            list3.append(element)

    for element in list2:
        if element not in list1:
            list4.append(element)

    print(list(set(list2) - set(list1)))
    return list3 + list4

def test3(list):
    string = ''.join(list)
    return string

def test4(list):
    for i in random(range(1,5)):
        print list[i]
        
def ciridentical(list1, list2):
    flag = 1
    for element in list1:
        if element not in list2:
            flag = 0
    if flag:
        print "identical\n"
    else:
        print "not identical\n"

def repfreq(list):
    dict =  {}
    count = 1
    for element in list:
        if element not in dict.keys():
            dict[element] = count
        else:
            dict[element] = count +1
    print dict
    ctr = collections.Counter(list)
    print ctr
    print set(list)

def test5(list):
    list1 = []
    number = 5
    for i in range(1,number+1):
        for element in list:
            list1.append(element+str(i))
            
            
    return list1
def commonelements(list1, list2):
    list3 = []
    for element in list1:
        if element in list2:
            list3.append(element)
    print (set(list1) & set(list2))      
    return list3
    
def test6(list):
    string = ''
    for element in list:
        string = string + str(element)
    return string

def largest(list):
    list.sort()
    return list[1]

def test7(list1, list2):
    list1[-1:] = list2
    return list1
    
def iterate2lists(list1, list2):
    for (element1, element2) in zip(list1, list2):
        print (element1, element2)
    
if __name__ == '__main__':
    #print test(['abc', 'xyz', 'aba', '1221', '3443'])
    #print removedup(['abc', 'xyz', 'aba','laskdfjlas','oqweuro', 'lzxcv', 'uyoeu'], 3)
    #print common_mem(['v', 'e', 'n', 'k', 'a', 't'],['n', 'a', 'i', 'n', 'i'])
    #print test1([7,8, 120, 25, 44, 20, 27])
    #print test2()
    #print (list(itertools.permutations([1,2,3])))
    #print difference([1,2,3,4], [3,4,5,6])
    #print test3(['v', 'e', 'n', 'k', 'a', 't'])
    #test4(['v', 'e', 'n', 'k', 'a', 't'])
    #print ciridentical([1,2,3,4], [3,4,1,2])
    #print largest([3,4,1,2])
    #print repfreq([1,2,3,3,4,4,4,5,6])
    #print test5(['p','q'])
    #print commonelements([1,2,3,4], [1,3,2])
    #print test6([11,33,50])
    #print test7([1, 3, 5, 7, 9, 10], [2, 4, 6, 8])
    iterate2lists([1, 3, 5, 7, 9, 10], [2, 4, 6, 8])
