class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val: index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
    

# # 2026/02/27

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         prevMap = {} # val : index
#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in prevMap:
#                 return [prevMap[diff], i]
#             prevMap[n] = i
#         return


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         seen = {} # num : index
#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in seen:
#                 return [seen[diff],i]
#             seen[n] = i