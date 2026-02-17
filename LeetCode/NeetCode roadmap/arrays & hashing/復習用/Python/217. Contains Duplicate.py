class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for n in nums:
            if count.get(n, 0) > 0:
                return True
            else:
                return False
            
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#         for n in nums:
#             if n in seen:
#                 return True
#             seen.add(n)
#         return False

# # #20260217

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#         for n in nums:
#             if n in seen:
#                 return True
#             seen.add(n)
#         return False