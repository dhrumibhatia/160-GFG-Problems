
arr = [12, 35, 1, 10, 34, 1]
# arr = [10,5,10]
arr = [1,2,3,3,3]
def second_largest(arr):
    if len(set(arr)) == 1:
        return -1
    elif len(set(arr)) == 2:
        return min(arr)
    else:   
        arr.sort()
        if arr[-1] in arr[0:-1]:
            co = [1 for i in arr if i==arr[-1]]
            return arr[-(len(co)+1)]
        return arr[-2]
print(second_largest(arr))
