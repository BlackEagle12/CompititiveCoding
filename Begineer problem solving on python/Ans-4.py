import math

def check_prime(n):
    root = math.floor(math.sqrt(n))
    for i in range(2,root + 1):
        if (n % i == 0):
            return False

    return True

n = int(input())

if(check_prime(n)):
    print(n,"IS PRIME")
else:
    print(n,"IS NOT PRIME")