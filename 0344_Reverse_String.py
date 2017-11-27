
class Solution(object):
    def reverseString(self, s):
        return s[::-1]


str = input()
solution = Solution()
str = solution.reverseString(str)
print(str)