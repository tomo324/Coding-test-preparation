class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashset = set()
        for s in strs:
            s_sorted = sorted(s)
        for a in s_sorted:
            hashset.add(a)
        for i in range(len(hashset)):
            group = []
            for s in strs:
                s_s = sorted(s)
                if s_s in hashset:
                    group.append(s)
        print(group)


                