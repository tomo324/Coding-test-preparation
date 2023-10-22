# https://leetcode.com/problems/fibonacci-number/description/

class Solution:
    def fib(self, n: int) -> int:
        def f(n, memo={}):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n == 1:
                return 1
            res = f(n - 1, memo) + f(n - 2, memo)
            memo[n] = res
            return res
        print(f(n))
        return f(n)

solution = Solution()
solution.fib(4)