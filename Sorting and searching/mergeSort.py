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

def mergeSort(arr,left,right):

	if(left == right):
		li = []
		li.append(arr[left])
		return li

	mid = left + right // 2
	
	leftSortedHalf = mergeSort(arr, left, mid)
	
	rightSortedHalf = mergeSort(arr, mid + 1, right)
	
	output = merge(leftSortedHalf, rightSortedHalf)

	return output


li = input().split(' ')
size = len(li)
for i in range(0,size):
	li[i] = int(li[i])

sortedLi = mergeSort(li, 0, size-1)

print(li)
print(sortedLi)