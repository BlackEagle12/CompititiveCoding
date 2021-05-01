def insersionSort(arr):
    n = len(arr)
    for i in range(1,n):
        j =i-1
        element = arr[i]
        while j >= 0 and arr[j] > element:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = element

arr = [5,4,3,2,1]
insersionSort(arr)
print(arr)

