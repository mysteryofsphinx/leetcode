class Solution(object):
    def judgeCircle(self, moves):
        if moves.count('U', 0, len(moves)) == moves.count('D', 0, len(moves)) and \
            moves.count('R', 0, len(moves)) == moves.count('L', 0, len(moves)):
                return True
        else :
            return False


x = str(input())
y = Solution()
flag = Solution.judgeCircle(y, x)
print(flag)