# -*- coding: utf-8 -*-

class Solution(object):
    def findDuplicates(self, nums):
        res = []
        for x in nums:
            nums[abs(x)-1] *= -1
            if(nums[abs(x)-1] > 0):
                res.append(abs(x))
        return res


nums = input()
numlist = nums.split()
solution = Solution()
numlist = [int(numlist[i]) for i in range(len(numlist))]
res = solution.findDuplicates(numlist)
print(res)


