def bubbleSort(arr):
    n = len(arr)
    for j in range(0,n-1):
        swap = False
        for i in range(0,n- 1):
            if(arr[i] > arr[i + 1]):
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swap = True
        n = n-1
        if(swap == False):
            return



arr = [5,4,3,2,1]
bubbleSort(arr)

print(arr)