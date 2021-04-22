str = input()

dis = {}

length = len(str)

for i in range(0, length):
    if dis.get(str[i]) == None: 
        dis[str[i]] = 1
    else:
        dis[str[i]] += 1

result = []

for key in dis.keys():
    if dis[key] == 1:
        result.append(key)

print(result)
