
def word_count(str1):
    counts = dict()
    words = str1.split()

    for word in words:
        if word in counts:
            counts[word] +=1
        else:
            counts[word] = 1
    return counts

print( word_count('jumping rocks and jumping is fun and rocks')) 

