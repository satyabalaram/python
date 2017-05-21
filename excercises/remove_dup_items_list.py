
dup_items = set()

def function (items):
    for i in items:
        if i not in dup_items:
            dup_items.add(i)
    return dup_items


print function([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1), (1, 2), (4, 4)])
