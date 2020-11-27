"""
coding: utf8
@time: 2020/11/27 16:43
@author: cjr
@file: 打家劫舍.py
题目链接：https://leetcode-cn.com/problems/house-robber/
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        dp = [[0] * 2 for i in range(n)]
        # 其中0表示这个房子不偷，1表示这个房子不偷
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1, n):
            # 如果这个房子不偷，那么这个房子的结果就是上一个房子偷或者不偷的最大值
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            # 如果这个房子偷，那么这个房子的结果就是上个房子不偷加上这个房子有的钱
            dp[i][1] = dp[i][0] + nums[i]
        return max(dp[-1][0], dp[-1][1])



