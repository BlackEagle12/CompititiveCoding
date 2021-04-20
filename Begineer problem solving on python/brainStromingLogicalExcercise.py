
a = int(input())
b = int(input())

def powerWithRecursion(a,b):
    if (b == 0):
        return 1
    if (b == 1):
        return a

    temp = powerWithRecursion(a,b//2)

    if (b % 2 == 0):
        return temp * temp
    else:
        return temp * temp * a

print(a, "power", b, "In Most OPTIMIZE Way :", powerWithRecursion(a,b))