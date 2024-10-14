class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            counter = [0] * 26 # mapping to [a ... z]
            for c in s:
                counter[ord(c) - ord("a")] += 1
            ans[tuple(counter)].append(s)
        return ans.values()