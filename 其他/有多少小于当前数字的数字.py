"""
coding: utf8
@time: 2020/10/26 8:43
@author: cjr
@file: 有多少小于当前数字的数字.py
题目链接：https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        排序之后
        下标与后面元素数量是相同的
        重复元素是一个下标。
        :param nums:
        :return:
        """
        new_nums = sorted(nums)
        res = []
        for num in nums:
            res.append(new_nums.index(num))
        return res
