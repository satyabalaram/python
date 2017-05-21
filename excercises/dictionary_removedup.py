d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

c = dict()
for keys, values in d1.items():
    for keys1, values1 in d2.items():
        if keys not in d2.keys():
            c[keys]=values


c.update(d2)
print c
        
        
