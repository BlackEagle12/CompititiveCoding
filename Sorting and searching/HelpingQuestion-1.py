
import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#please remove above 3 lines if you are using teminal for input and output

def merge(li1,li2):
	total = len(li1) + len(li2)
	n = len(li1)
	m = len(li2)
	outLi = [0]*total
	i = 0
	j = 0
	k = 0
	while i < total :
		if(k == m or (j < n and li1[j] < li2[k])):
			outLi[i] = li1[j]
			j += 1
		else :
			outLi[i] = li2[k]
			k +=1
		i += 1

	return outLi

li1 = input().split(' ')
size = len(li1)
for i in range(0,size):
	li1[i] = int(li1[i])

li2 = input().split(' ')
size = len(li2)
for i in range(0,size):
	li2[i] = int(li2[i])

print(merge(li1,li2))