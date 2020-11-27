"""
coding: utf8
@time: 2020/11/27 14:38
@author: cjr
@file: 乘积最大子数组.py
题目链接：https://leetcode-cn.com/problems/maximum-product-subarray/
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        动态规划
        :param nums:
        :return:
        """
        maxx = minn = res = nums[0]
        for i in range(1, len(nums)):
            # 因为有负数的存在，负数乘以大的会变小，而负数乘以小的更大
            # 所以在值为负数的时候应该将，最大值和最小值调换，再求值
            if nums[i] < 0:
                maxx, minn = minn, maxx
            maxx = max(maxx * nums[i], nums[i])
            # 必须维护一个最小值，因为当最小值为负数的时候，如果下一个值也是负数，那么相乘之后也有可能是答案
            minn = min(minn * nums[i], nums[i])
            res = max(res, maxx)
        return res
