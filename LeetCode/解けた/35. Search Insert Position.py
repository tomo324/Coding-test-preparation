"""
https://leetcode.com/problems/search-insert-position/description/

42分25秒

二分探索が分かれば解ける
二分探索の方法を調べるのに時間がかかってしまった
基本的なアルゴリズムの実装方法は覚えておいた方が良い
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums_list = nums
        if target not in nums:
            nums_list.append(target)
            nums_list.sort()
            return nums_list.index(target)
        else:
            left_index = 0
            right_index = len(nums) - 1
            while left_index <= right_index:
                mid_index = (left_index + right_index) // 2
                if nums[mid_index] == target:
                    return nums.index(target)
                elif nums[mid_index] < target:
                    left_index = mid_index + 1
                else:
                    right_index = mid_index - 1