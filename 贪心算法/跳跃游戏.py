"""
coding: utf8
@time: 2020/11/23 15:45
@author: cjr
@file: 跳跃游戏.py
题目链接：https://leetcode-cn.com/problems/jump-game/
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        贪心。从后往前遍历，只要最后一个能跳到终点就把最后的标志位往前移动，看能不能移动到最开始
        :param nums:
        :return:
        """
        if not nums:
            return False
        end = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= end:  # i + nums[i] 是当前可以到达的最大位置
                end = i
        return end == 0




