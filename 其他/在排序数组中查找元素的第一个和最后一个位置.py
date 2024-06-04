"""
coding: utf8
@time: 2020/12/1 20:50
@author: cjr
@file: 在排序数组中查找元素的第一个和最后一个位置.py
题目链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def binary_search(nums, target, lower):
            left, right = 0, len(nums) - 1
            res = len(nums)
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target or (nums[mid] >= target and lower):
                    right = mid - 1
                    res = mid
                else:
                    left = mid + 1
            return res

        left_idx = binary_search(nums, target, True)
        right_idx = binary_search(nums, target, False) - 1
        if left_idx <= right_idx < len(nums) and nums[left_idx] == target and nums[right_idx] == target:
            return [left_idx, right_idx]
        return [-1, -1]



