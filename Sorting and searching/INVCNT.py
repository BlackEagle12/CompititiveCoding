import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

# mergesort approach
def merge(arr1,arr2):
	n = len(arr1)
	m = len(arr2)
	length = n + m

	arr = [0]*length
	i = 0
	j = 0
	k = 0
	count = 0
	while(k < length):
		if(j>=m or (i<n and arr1[i] < arr2[j])):
			arr[k] = arr1[i]
			k = k + 1
			i = i +1
		else:
			arr[k] = arr2[j]
			count += n - i
			k = k + 1
			j = j + 1

	return arr,count


def mergeSortAndCount(arr,start,end):

	if(start == end):
		li = []
		li.append(arr[start])
		return li, 0

	mid = start + (end - start)//2
	
	leftSortedHalf, leftCount = mergeSortAndCount(arr,start,mid)
	rightSortedHalf, rightCount = mergeSortAndCount(arr,mid + 1,end)

	arr,count = merge(leftSortedHalf, rightSortedHalf)

	return arr,count + leftCount + rightCount


t = int(input())
for i in range(0,t):
	ch = input()
	n = int(input())
	li = []
	for j in range(0,n):
		li.append(int(input()))

	arr,count = mergeSortAndCount(li,0,len(li) - 1)
	print(count)
