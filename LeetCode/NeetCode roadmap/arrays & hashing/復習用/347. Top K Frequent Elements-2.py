class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # num : count
        freq = [[] for _ in range(len(nums) + 1)] # i=count : num
        
        # numごとの出現回数をカウント
        for n in nums:
            count[n] = count.get(n, 0) + 1
        # freqでバケットソート
        for n, c in count.items():
            freq[c].append(n)
        # 後ろからk個取得
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res