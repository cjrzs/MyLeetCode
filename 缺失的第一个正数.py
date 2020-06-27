'''
coding:utf8
@Time : 2020/6/27 17:28
@Author : cjr
@File : 缺失的第一个正数.py
题目链接：https://leetcode-cn.com/problems/first-missing-positive/
'''
import typing


class Solution:
    def firstMissingPositive(self, nums: typing.List[int]) -> int:
        """
        把字典标记所有大于nums中大于0的数，
        然后判断标记是否在（1， n + 1）中
        :param nums:
        :return:
        """
        n = len(nums)
        d = {i: i for i in nums if i > 0}
        for i in range(1, n + 1):
            if i not in d:
                return i
        return n + 1



