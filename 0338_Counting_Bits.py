

class Solution(object):
    def countBits(self, num):
        ans = [0]*(num+1)
        for i in range(1,num+1):
            index = int(i & (i - 1))
            ans[i] = ans[index] + 1;
        return ans


num = int(input())
solution = Solution()
ans = solution.countBits(num)
for x in ans:
    print(x)
