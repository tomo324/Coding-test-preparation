class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # num: count
        lst = [[] for _ in range(len(nums)+1)] # lst[count] = num: List

        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            lst[c].append(n)
        res = []
        for i in range(len(lst) - 1, 0, -1):
            res += lst[i]
            if len(res) == k:
                return res