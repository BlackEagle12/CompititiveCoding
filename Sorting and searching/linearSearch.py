import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#please remove above 3 lines if you are using teminal for input and output

def linearSearch(li, ele):
	n = len(li)
	for x in range(0,n):
		if li[x] == ele:
			return x + 1;

li = [int(x) for x in input().split(' ')]

print(linearSearch(li,int(input())));