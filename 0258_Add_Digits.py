class Solution:
    def addDigits(self, num):
        
        return (1 + (num - 1) % 9) if num != 0 else 0

num = int(input())
solution = Solution()
print(solution.addDigits(num))