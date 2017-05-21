
def isprime(n):
    if (n == 1):
        return True
    elif (n == 2):
        return False
    else:
        for i in range (2,n):
            if (n % i ==0):
                return False
        return True

print isprime(5)
