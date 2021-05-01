
def findMInimumElementIndex(arr, start):
    min_index = start
    start += 1
    while(start < len(arr)):
        if(arr[start] < arr[min_index]):
            min_index = start
        start +=1

    return min_index

def swap(arr, ind1, ind2):
    temp = arr[ind1]
    arr[ind1] = arr[ind2]
    arr[ind2] = temp

def selectionSort(arr):
    i = 0
    while(i < len(arr)):
        minIndex = findMInimumElementIndex(arr, i)
        swap(arr, i,minIndex)
        i += 1

arr = [5,4,3,2,1]
selectionSort(arr)
print(arr)

