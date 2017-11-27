
class Solution:
    def selfDividingNumbers(self, left, right):
        ans = []
        for i in range(left, right+1):
            tmp = i
            flag = True
            while tmp != 0:
                fac = tmp%10
                if fac == 0:
                    flag = False
                    break
                if i%fac != 0 :
                    flag = False
                    break
                tmp = tmp // 10
            if flag == True:
                ans.append(i) 

        return ans               

left = int(input())
right = int(input())
solution = Solution()
ans = solution.selfDividingNumbers(left, right)
print(ans) 

# a better solution 
# class Solution(object):
#     def selfDividingNumbers(self, left, right):
#         is_self_dividing = lambda num: '0' not in str(num) and all([num % int(digit) == 0 for digit in str(num)])
#         return filter(is_self_dividing, range(left, right + 1))       