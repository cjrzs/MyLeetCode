"""
coding: utf8
@time: 2020/11/25 22:36
@author: cjr
@file: 颜色分类.py
题目链接：https://leetcode-cn.com/problems/sort-colors/
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        # 我们把最后结果定义为三部分 [0, zero), [zero, i), [two, len - 1]
        zero, two = 0, n
        while i < two:
            if nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
                i += 1
            elif nums[i] == 2:
                two -= 1
                nums[i], nums[two] = nums[two], nums[i]
            else:
                i += 1


