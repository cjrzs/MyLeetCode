"""
coding: utf8
@time: 2021/1/10 21:48
@author: cjr
@file: 汇总区间.py
题目链接：https://leetcode-cn.com/problems/summary-ranges/
"""
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        n = len(nums)
        i, j = 0, 0
        while j < n:
            while j < n - 1 and nums[j] + 1 == nums[j + 1]:
                j += 1
            tmp = [str(nums[i])]
            if nums[i] != nums[j]:
                tmp.append('->')
                tmp.append(str(nums[j]))
            res.append(''.join(tmp))
            j += 1
            i = j
        return res


