"""
coding: utf8
@time: 2020/10/22 22:34
@author: cjr
@file: 三数之和.py
题目链接：https://leetcode-cn.com/problems/3sum/
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        排序+双指针+左右夹逼

        :param nums:
        :return:
        """
        # 先排序
        nums.sort()
        res = []
        # 遍历一次
        for k in range(len(nums) - 2):
            # k是第一个数，它最小所以大于0直接就break
            if nums[k] > 0:
                break
            # 如果两个数字连着相等则可以直接跳过
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            # 初始化双指针，左右夹逼
            i, j = k + 1, len(nums) - 1
            while i < j:
                sums = nums[k] + nums[i] + nums[j]
                if sums > 0:
                    j -= 1
                    # 如果遇见相同的元素可以直接跳过
                    while i > j and nums[j] == nums[j + 1]:
                        j -= 1
                elif sums < 0:
                    i += 1
                    # 如果遇见相同的元素可以直接跳过
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i > j and nums[j] == nums[j + 1]:
                        j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
        return res


