

def check(lis, index, max):
    if lis[index] > lis[index + 1]:
        return False
    if index + 1 == max:
        return True
    
    return check(lis, index + 1, max)

inp = input()
lis = inp.split(" ")
max = len(lis)
for i in range (0, max):
    lis[i] = int(str(lis[i]))

if(check(lis, 0, max - 1)):
    print("YES")
else:
    print("No")

