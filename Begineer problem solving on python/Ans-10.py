
n = input().split(" ")

len = len(n)

lis = []

ans = 0

i = 0

while i < len :
    ele = int(n[i])
    ans = ans ^ ele
    i = i + 1
    lis.append(ele)

print("In the list ", lis, "unique element is", ans)


