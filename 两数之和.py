"""
coding: utf8
@time: 2020/10/21 21:12
@author: cjr
@file: 两数之和.py
题目链接：https://leetcode-cn.com/problems/two-sum/
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        使用一个字典存储值与下标
        每次都检测目标值减去当前值剩下的结果在不在字典中
        在的话就找到了，取出两个下标即可
        :param nums:
        :param target:
        :return:
        """
        tmp = {}
        for i in range(len(nums)):
            sum_res = target - nums[i]
            if sum_res in tmp:
                return [tmp[sum_res], i]
            tmp[nums[i]] = i


