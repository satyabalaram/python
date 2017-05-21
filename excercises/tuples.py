tuplex = (4, 6, 2, 8, 3, 1)

tuplex = tuplex + (9,)
print tuplex

tuplex = tuplex[:5] + (15, 20, 25) 
print tuplex
listx = list(tuplex)
listx.append(30)

tuplex = tuple(listx)
print tuplex

tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str =  ''.join(tup)
print(str)

print tuplex[4], '\t', tuplex[-4]

#count repeated elements in tuple

tuplex1 = 2, 4, 5, 6, 2, 3, 4, 4, 7

count = tuplex1.count(4)
print count


print (4 in tuplex1)

# remove element from tuple, #tuples are immutable, so you can not remove elements

tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
tuplex = tuplex[:2] + tuplex[3:]
print tuplex
listx = list(tuplex)
listx.remove("c")
tuplex = tuple(listx)
print tuplex
print tuplex.index("r")
print len(tuplex)

#convert tuple to dict

tuplex = ((2, "w"),(3, "r"))
print(dict((y, x) for x, y in tuplex))

x = ("w3resource")
y = reversed(x)
print tuple(y)

l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
d = dict()

for a, b in l:
    d.setdefault(a,[]).append(b)

print d
