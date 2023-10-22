class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0)
        for i in range(len(cost) - 4, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])

        print(min(cost[0], cost[1]))
        return min(cost[0], cost[1])



n = [1,100,1,1,1,100,1,1,100,1]
solution = Solution()
solution.minCostClimbingStairs(n)


'''
costのlength大きすぎ、再帰できない。解く前に確認すべきだった。

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        def climb(cost, paid, i):
            paid = paid + cost[i]
            if i >= (len(cost) - 2):
                return paid
            oneStep = i + 1
            twoStep = i + 2
            res = min(climb(cost, paid, oneStep), climb(cost, paid, twoStep))
            print(res)
            return res
        paid = 0
        result = min(climb(cost, paid, 0), climb(cost, paid, 1))
        print(result)
        return result

        import sys
sys.setrecursionlimit(10 ** 6)

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        memo = {}
        paid = 0
        def climb(i, paid):
            paid += cost[i]
            if i in memo:
                return memo[i]
            if i >= (len(cost) - 2):
                return paid
            plusOne = i + 1
            plusTwo = i + 2
            res = min(climb(plusOne, paid), climb(plusTwo, paid))
            memo[i] = res
            return res
        result = min(climb(0, paid), climb(1, paid))
        print(result)
        return result
'''
