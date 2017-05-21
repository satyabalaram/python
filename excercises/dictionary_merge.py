
d1 = {(1,2), (1,3), (2,2)}
d2 = {(2,3), (4,5), (5,6)}

def create_dict(d1, d2):
    d = d1.copy()
    d.update(d2)

    return d
        
print create_dict(d1,d2)
