
N = int(input())

for i in range(1,N+1):
    for j in range(N,i,-1):
        print("   ", end="")  #one more space then below loops bcz its one space is cover by character

    for j in range(1,i+1):
        print(j, end="  ")

    for j in range(i-1,0,-1):
        print(j, end="  ")

    print()
