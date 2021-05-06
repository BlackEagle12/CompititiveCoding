import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#please remove above 3 lines if you are using teminal for input and output

def binarySearchOnSortedShiftedArray(arr,ele):

	start = 0
	end = len(arr) - 1
	
	while start <= end:

		mid = start + (end - start)//2
		if arr[mid] == ele:
			return mid + 1

		elif arr[mid] >= arr[start]:
			if ele < arr[mid] and ele >= arr[start] :
				end = mid - 1
			else:
				start = mid + 1
		
		else:
			if ele > arr[mid] and ele <= arr[end]:
				start = mid + 1
			else:
				end = mid - 1

	return - 1

li = [int(x) for x in input().split(' ')]

print(binarySearchOnSortedShiftedArray(li, int(input())))