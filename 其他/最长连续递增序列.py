"""
coding: utf8
@time: 2021/2/28 22:48
@author: cjr
@file: 最长连续递增序列.py
题目链接：https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/
"""
from typing import List


class Solution:
    """
    朴实无华的双指针
    """
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            j = i + 1
            while j < n and nums[j] > nums[j - 1]:
                j += 1
            res = max(res, j - i)
        return res

