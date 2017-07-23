start = 50
end = 100
results = []

for n in range(start + 1, end):
    t = list(str(n))
    # set gives you only one output if the numbers are same (ex: 5,5 will return 5). Len of that would be
    # one compare to rest of them
    if len(t) == len(set(t)):
        results.append(n)

print 'Results:', results
