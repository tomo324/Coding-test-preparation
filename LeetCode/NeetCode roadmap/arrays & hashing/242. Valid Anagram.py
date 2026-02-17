class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
    

# #20260217

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         countS, countT = {}, {}

#         # ちょっと冗長
#         for c in s:
#             countS[c] = 1 + countS.get(c, 0)
#         for c in t:
#             countT[c] = 1 + countT.get(c, 0)
        
#         for s in countS:
#             if countS.get(s, 0) != countT.get(s, 0):
#                 return False
#         return True