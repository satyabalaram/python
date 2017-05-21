n = set([0,1,2,3,4])

for i in n:
    print i

n.add("5")
print n

n.remove("5")
print n

n.discard(2)
print n

setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
seta = setx & sety
setr = setx | sety
print(seta)
print (setr)
setb = setr - seta
print setb
setc = setx ^ sety
print setc

setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = set(["mango"])

issubset = setx <= sety
print(issubset)
issuperset = setx >= sety
print(issuperset)
issubset = setz <= sety
print(issubset)
issuperset = sety >= setz
print(issuperset)

seta = set([5, 10, 3, 15, 2, 20])
#Find maximum value
print(max(seta))
#Find minimum value
print(min(seta))
print(len(seta))
