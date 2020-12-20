"""
coding: utf8
@time: 2020/12/20 22:26
@author: cjr
@file: 删除子数组的最大得分.py
题目链接：https://leetcode-cn.com/problems/maximum-erasure-value/
"""
from typing import *


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        直接暴力法硬怼 毫无疑问超时了  因为题目给出了数据规模在 10^5
        :param nums:
        :return:
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        visited = set()
        max_res = 0
        res = 0
        for i in range(n):
            for j in range(i, n):
                if nums[j] not in visited:
                    max_res += nums[j]
                    visited.add(nums[j])
                else:
                    res = max(max_res, res)
                    max_res = 0
                    visited.clear()
                    break
        return res

    def maximumUniqueSubarray2(self, nums: List[int]) -> int:
        """
        滑动窗口模板 直接套就行了
        :param nums:
        :return:
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        counters = [0] * 10001
        cur = 0
        res = 0
        l, r = 0, 0
        while r < n:
            cur += nums[r]
            counters[nums[r]] += 1
            while l < r and counters[nums[r]] > 1:
                cur -= nums[l]
                counters[nums[l]] -= 1
                l += 1
            res = max(res, cur)
            r += 1
        return res
