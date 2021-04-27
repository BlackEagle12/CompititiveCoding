n = input().split(" ")

length = len(n)
lis =[]

lis.append(int(n[0]))
for i in range(1, length):
    ele = int(n[i])
    lis.append(ele)
    lis[i] += lis[i - 1]

l = int(input())
r = int(input())

print(lis[r] - lis[l] + int(n[l]))

