"""
coding: utf8
@time: 2021/2/28 22:49
@author: cjr
@file: 最长递增子序列的个数.py
题目链接：https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/
"""
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # f[i]表示以i结尾的最长上升子序列长度
        # g[i]表示以i结尾的最长上升子序列个数
        f, g = [0] * n, [0] * n
        # maxl记录最大长度，cnt记录最大个数
        maxl, cnt = 0, 0
        for i in range(n):
            f[i] = g[i] = 1
            for j in range(i):
                # 判断序列是上升的
                if nums[j] < nums[i]:
                    # 动态规划求当前的最长上升子序列长度和个数
                    # 当前i的最长上升子序列长度就等于
                    # 他前一个元素为止的最长上升子序列长度加一
                    # 个数的话就是如果有两个长度相等最长上升子序列
                    # 个数就要加上g[j]
                    if f[i] < f[j] + 1:
                        f[i] = f[j] + 1
                        g[i] = g[j]
                    elif f[i] == f[j] + 1:
                        g[i] += g[j]
            # 如果当前长度大于最大长度则更新当前长度
            # 并更新最大长度个数
            if maxl < f[i]:
                maxl = max(maxl, f[i])
                cnt = g[i]
            # 如果当前长度等于最大长度则最大个数加上g[i]
            elif maxl == f[i]:
                cnt += g[i]
        return cnt



