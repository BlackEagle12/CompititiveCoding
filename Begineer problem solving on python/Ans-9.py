

def check_ways(n,step,path):

    if n < step:
        return
    if n == step:
        print(path)
        return

    check_ways(n, step+2, "2 " + path)
    check_ways(n, step+1, "1 " + path)

n = int(input())
check_ways(n, 0, "")

