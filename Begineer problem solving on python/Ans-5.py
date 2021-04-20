
a = int(input())
b = int(input())

# With loop

def powerWithLoop(a,b):
    pow = 1

    if(b==0):
        return 1
    while b > 0:
        pow *= a
        b -= 1

    return pow

# With recursion

def powerWithRecursion(a,b):
    if (b == 0):
        return 1
    if (b == 1):
        return a
    return a * powerWithRecursion(a,b-1)

print(a, "power", b, "via iteration :", powerWithLoop(a,b))
print(a, "power", b, "via recursion :", powerWithRecursion(a,b))
