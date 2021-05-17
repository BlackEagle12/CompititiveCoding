#given a perfact square value s (e.g. 25 = 5*5) between 1 to 10^9 find its squareroot... 

import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')


def findSqrt(ele):
	start = 0
	end = ele

	while(start <= end):
		mid = start + (end - start)//2
		squareMid = mid*mid
		if squareMid == ele:
			return mid
		elif squareMid < ele:
			start = mid + 1
		else:
			end = mid - 1

	return start

s = int(input())

print(findSqrt(s))