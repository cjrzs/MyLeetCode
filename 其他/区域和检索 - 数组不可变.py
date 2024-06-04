"""
coding: utf8
@time: 2021/3/1 21:29
@author: cjr
@file: 区域和检索 - 数组不可变.py
题目链接：https://leetcode-cn.com/problems/range-sum-query-immutable/
"""
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = [0] + nums
        f = [0] * (len(self.nums) + 1)
        f[0] = self.nums[0]
        for i in range(1, len(self.nums)):
            f[i] = self.nums[i] + f[i - 1]
        self.f = f

    def sumRange(self, i: int, j: int) -> int:
        return self.f[j + 1] - self.f[i]






