"""
coding:utf8
@Time : 2020/7/31 18:22 
@Author : CJR  
@File : 魔术索引.py
题目链接：https://leetcode-cn.com/problems/magic-index-lcci/
"""
from typing import List


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            if nums[i] == i:
                res.append(i)
        return -1 if not res else min(res)



