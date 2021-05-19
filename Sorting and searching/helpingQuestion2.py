import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#please remove above 3 lines if you are using teminal for input and output

def segrigateElements(arr, ele):
	n = len(li)
	m = 0
	
	for x in range(0,n):
		if arr[x] <= arr[ele]:
			arr[m], arr[x] = arr[x], arr[m]
			m += 1
			print(arr)
	arr[m],arr[ele] = arr[ele], arr[m] 
			


li = input().split(' ')
size = len(li)
for i in range(0,size):
	li[i] = int(li[i])

segrigateElements(li, 2)

print(li)