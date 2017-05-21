
sdict = {}

def charector_count(str1):
    for i in str1:
        keys = sdict.keys()
        if i in keys:
            sdict[i] +=1
        else:
            sdict[i]=1
    return sdict

    
print (charector_count('apple'))
