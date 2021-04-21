
N = int(input())

def display(n):
    if(n == 0):
        return
    print(n)
    display(n-1)

display(N)