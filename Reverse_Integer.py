class Solution(object):
    def reverse(self, x):
        flag = False
        if x < 0:
            flag = True
        x = abs(x)
        x = str(x)
        y = int(x[::-1])
        if y > 2147483647:
            return 0
        else:
            if flag == True:
                return -y
            else :
                return y


x = int(input())
t = Solution()
y = Solution.reverse(t, x)
print(y)