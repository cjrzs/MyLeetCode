"""
coding: utf8
@time: 2020/11/27 12:54
@author: cjr
@file: 最大子序和.py
https://leetcode-cn.com/problems/maximum-subarray/
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        动态规划
        状态转移方程: dp[i] = max(0, dp[i - 1]) + nums[i]
        因为如果上一个小于0的话，就把当前最大值就是等于当前的值nums[i]了。
        :param nums:
        :return:
        """
        dp = nums
        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i - 1]) + nums[i]
        return max(dp)


