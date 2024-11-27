#solution 1
# remeber the (array in place) basically we are not allowed to make the new array.
arr = [1, 2, 0, 4, 3, 0, 5, 0]
arr = [3,5 ,0, 0, 4]
zero_count = 0
i = 0
while i < len(arr):
    if arr[i] == 0:
        arr.pop(i)
        zero_count += 1
    else:
        i += 1
arr.extend([0] * zero_count)


class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        count = 0  

        # Traverse the array. If the element encountered is non-zero, then
        # replace the element at index 'count' with this element
        for i in range(n):
            if arr[i] != 0:
                arr[count] = arr[i]
                count += 1

        # Now all non-zero elements have been shifted to the front and 'count' is
        # set to the index of the first 0. Make all elements from count to end 0
        while count < n:
            arr[count] = 0
            count += 1

arr = [1, 2, 0, 4, 3, 0, 5, 0]
solution = Solution()
solution.pushZerosToEnd(arr)
print(arr) 

arr = [10, 20, 30]
solution.pushZerosToEnd(arr)
print(arr)  

arr = [0, 0]
solution.pushZerosToEnd(arr)
print(arr) 
intt = [i for i in arr if i != 0] + [0] * arr.count(0)
print(intt)
