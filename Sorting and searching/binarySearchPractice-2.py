## Given An unsorted list a[i] 
## find any element a[i] such that
## a[i-1] > a[i] && a[i + 1] > a[i]

import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

def findPeak(li):
	n = len(li)
	start, end = 0, n-1

	while(start <= end):

		mid = start + (end - start)// 2

		if li[mid] > li[mid-1] and li[mid] > li[mid-1]:
			return mid

		if li[mid] > li[mid + 1] :
			end = mid - 1
		else:
			start = mid + 1

	return start


li = [int(x) for x in input().split(' ')]

index = findPeak(li)
print(index)


