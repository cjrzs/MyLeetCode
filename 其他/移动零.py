"""
coding: utf8
@time: 2020/10/20 22:44
@author: cjr
@file: 移动零.py
题目链接:https://leetcode-cn.com/problems/move-zeroes/
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while i < len(nums):
            if nums[i] != 0:
                nums[j] = nums[i]
                # 当i不等于j时候说明此时nums[i]一定已经被移动了，所以要置为0
                if i != j:
                    nums[i] = 0
                j += 1
            i += 1

