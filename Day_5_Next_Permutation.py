arr = [2, 4, 1, 7, 5, 0]

def nextPermutation(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    pivot = -1
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            pivot = i
            break
    
    if pivot == -1:
        arr.reverse()
        return arr
    

    for i in range(n - 1, pivot, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break
    
    arr[pivot + 1:] = reversed(arr[pivot + 1:])
    return arr


arr1 = [2, 4, 1, 7, 5, 0]
print(nextPermutation(arr1))  

arr2 = [3, 2, 1]
print(nextPermutation(arr2))  

arr3 = [3, 4, 2, 5, 1]
print(nextPermutation(arr3)) 