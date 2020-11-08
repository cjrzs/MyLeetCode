"""
coding: utf8
@time: 2020/11/8 23:00
@author: cjr
@file: 全排列.py
题目链接： https://leetcode-cn.com/problems/permutations/
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        本题中要求去除重复的元素，
        那我们就先排序，利用当前元素和上一元素是否相同判断是否重复。用一个备忘录记录下元素是否使用
        :param nums:
        :return:
        """
        nums.sort()
        res = []
        check = [0] * len(nums)

        def dfs(path, check):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                # 元素使用过则跳过
                if check[i] == 1:
                    continue
                # 从第二个元素开始如果与前一个相等并且前一个被使用过要剪支
                if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 1:
                    continue
                check[i] = 1
                dfs(path+[nums[i]], check)
                check[i] = 0
        dfs([], check)
        return res
