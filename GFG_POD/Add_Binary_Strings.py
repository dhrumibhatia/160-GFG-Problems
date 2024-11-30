class Solution:
    def addBinary(self, s1, s2):
        re = int(s1, 2) + int(s2, 2)
        return bin(re)[2:]

s1 = "1101"
s2 = "111"
solution = Solution()
result = solution.addBinary(s1, s2)
print(result) 