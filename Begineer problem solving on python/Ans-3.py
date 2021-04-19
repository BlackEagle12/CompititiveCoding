num = input()
TotalDigit = len(num)
num = int(num)
temp = num
sum = 0

while (num > 0):
    digit = num % 10
    sum += digit**TotalDigit
    num //= 10

print("Sum", sum)
if(sum == temp):
    print("YES")
else:
    print("NO")