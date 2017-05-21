
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b =[]
num = int(raw_input("chose a number between 1 and 100\n"))

for n in a:
    if n  < num :
      b.append(n)
        

print b
