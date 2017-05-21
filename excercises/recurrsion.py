def recursive_list_sum(num_List):
    total = 0
    for element in num_List:
        if type(element) == type([]):
            total = total + recursive_list_sum(element)
        else:
            total = total+element
    return total

print(recursive_list_sum([1, 2, [3,4], [5,6]]))


def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  else:
    return (fibonacci(n - 1) + (fibonacci(n - 2)))

print(fibonacci(7))
