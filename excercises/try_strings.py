def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           continue
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brow Fox')

def unique_list(list1):
    unique_list = set(list1)
    x = []
    for i in list1:
        if i not in x:
            x.append(i)
    return x
    #return unique_list

list1 = [1,2,3,3,3,3,4,5]
print unique_list(list1)

def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangle(6)

def sort_seq(string1):
    words = []
    for i in string1:
        words = string1.split('-')
        
    words.sort()
    return '-'.join(words)

print sort_seq("green-red-yellow-black-white")




