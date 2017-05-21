from collections import Counter

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

c = dict()
for keys, values in d1.items():
    for keys1, values1 in d2.items():
        if keys1 ==  keys:
            c[keys]= d1[keys] + d2[keys1]
        elif keys1 not in d1.keys() and keys not in d2.keys():
            c[keys1] = d2[keys1]
            c[keys] = d1[keys]
       
print c
        
d = Counter(d1) + Counter(d2)
print d
        
        
