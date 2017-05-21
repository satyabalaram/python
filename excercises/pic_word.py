import random

# read all the list of words
words = []
with open('sowpods.txt', 'r') as f:
        line = f.readline().strip()
        for line in f:
                words.append(line)

# generate a random number
random_index = random.randint(0, len(words))

# take the word
print("Random word: ", words[random_index])
        

        
        
