# https://leetcode.com/problems/climbing-stairs/description/

import sys
sys.setrecursionlimit(10 ** 6)

class Solution:
    def climbStairs(self, n: int) -> int:
        result = 0
        def oneStep(n, result, memo={}):
            if n in memo:
                return memo[n]
            if n == 0:
                result += 1
                return result
            if n <= 0:
                return result
            ans = oneStep(n-1, result, memo) + oneStep(n-2, result, memo)
            memo[n] = ans
            return ans
        res = oneStep(n, result)
        print(res)
        return res


n = 44
solution = Solution()
climb = solution.climbStairs(n)
