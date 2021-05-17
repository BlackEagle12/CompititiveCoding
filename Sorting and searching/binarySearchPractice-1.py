
## given a sorted list and an integer x 
## find the first value in the list which is grater or equal to x

import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

def findElement(li, tar):

	n = len(li)
	start = 0
	end = n-1

	while(start <= end):

		mid = start + (end-start)//2
		
		if tar >= li[mid] :
			start = mid + 1
		else :
			end = mid - 1

	return start




li = [int(x) for x in input().split(' ')]
target = int(input())

index = findElement(li, target)
print(index)