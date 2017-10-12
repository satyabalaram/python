from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

d3 = {}
for key, value in d1.items():
    for key1,value1 in d2.items():
        if key == key1:
            d3[key] = value + value1
        elif key not in d3.keys():
            d3[key] = value
        elif key1 not in d3.keys():
            d3[key1] = value1

print d3

d4 = {}
d4 = Counter(d1) + Counter(d2)
print dict(d4)
