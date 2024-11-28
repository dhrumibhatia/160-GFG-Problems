#we can use simple trick of python 
class Solution:
    def reverseArray(self, arr):
        return arr[::-1]


arr = [1, 2, 3, 4, 5]
solution = Solution()
reversed_arr = solution.reverseArray(arr)
print(reversed_arr)

# this solution is accepted as two pointer approach need to be implemented.
class Solution:
    def reverseArray(self, arr):
        # Two-pointer approach to reverse the array in place
        left = 0
        right = len(arr) - 1
        while left < right:
            # Swap elements at left and right indices
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            # Move pointers towards the center
            left += 1
            right -= 1
        return arr

# Example usage
arr = [1, 2, 3, 4, 5]
solution = Solution()
solution.reverseArray(arr)
print(arr)  # Output: [5, 4, 3, 2, 1]