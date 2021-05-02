import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#please remove above 3 lines if you are using teminal for input and output

def findMinMax(li):
	n = len(li)
	i = 0;
	min = sys.maxsize
	max = (-1 * min) -1
	
	while i < n:
		value = li[i]
		if min > value:
			min = value
		if max < value:
			max = value
		i += 1

	print("MIN : ", min, "MAX", max)
	return min, max

def bucketSort(li):
	
	minele,maxele = findMinMax(li)
	prefixSumList = [0]*(maxele - minele + 1)
	n = len(li)

	for i in range(0, n):
		prefixSumList[li[i] - minele] += 1

	print("PREFIX :", prefixSumList)
	for i in range(1, maxele - minele + 1):
		prefixSumList[i] += prefixSumList[i - 1]
	

	print("PREFIX SUM:", prefixSumList)
	out = [0]*n
	for i in range(n - 1, -1, -1):
		out[prefixSumList[li[i] - minele] - 1] = li[i]
		prefixSumList[li[i] - minele] -= 1
	
	return out
	

li = input().split(' ')

size = len(li)
for i in range(0,size):
	li[i] = int(li[i])

print("orignal List: ", li)
li = bucketSort(li)

print("FINAL OUTPUT :", li)

