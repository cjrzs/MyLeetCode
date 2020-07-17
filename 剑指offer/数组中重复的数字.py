'''
coding:utf8
@Time : 2020/7/15 14:41 
@Author : CJR  
@File : 数组中重复的数字.py
题目链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
'''
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        """
        排序后，从头开始判断是否有相邻两个元素相同，如果有则输出结果
        :param nums:
        :return:
        """
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i + 1]:
                return nums[i]

