"""
coding: utf8
@time: 2020/11/7 22:50
@author: cjr
@file: 子集.py
题目链接：https://leetcode-cn.com/problems/subsets/
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        直接套用回溯模板
        需要注意的是每一个元素都要加到结果里面
        :param nums:
        :return:
        """
        res = []

        def dfs(start, path):
            if start == len(nums):
                res.append(path[:])
                return
            # 先把元素加到结果
            dfs(start + 1, path)
            path.append(nums[start])
            dfs(start + 1, path)
            path.pop()

        dfs(0, [])
        return res

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        """
        暴力法   按照元素大小加入结果
        :param nums:
        :return:
        """
        ress = [[]]
        for num in nums:
            ress += [res + num for res in ress]
        return ress





