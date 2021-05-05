import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#please remove above 3 lines if you are using teminal for input and output

def binarySearchUsingrecursion(li,start,end,ele):
	mid = (start + end) // 2;
	
	if(start > end): return -1

	if(li[mid] == ele):
		return mid + 1
	elif li[mid] < ele:
		return binarySearchUsingrecursion(li,mid+1,end,ele)
	else:
		return binarySearchUsingrecursion(li,start,mid-1,ele)

def binarySearchUsingIteration(li,ele):
	i = 0;
	n = len(li)
	start,end = 0, n-1
	while True:
		mid = (start + end) // 2
		if(start > end): return -1
		
		elif li[mid] == ele:
			return mid + 1
		
		elif li[mid] < ele:
			start = mid + 1
		
		else:
			end = mid - 1


li = [int(x) for x in input().split(' ')]
ele = int(input())
print('Using Recursion', binarySearchUsingrecursion(li, 0, len(li)-1, ele))
print('Using Iteration', binarySearchUsingIteration(li, ele))