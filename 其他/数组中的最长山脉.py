"""
coding: utf8
@time: 2020/10/25 19:05
@author: cjr
@file: 数组中的最长山脉.py
题目链接：https://leetcode-cn.com/problems/longest-mountain-in-array/
"""
from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if not A:
            return 0
        n = len(A)
        left = [0] * n
        # 动态规划。 先算出左边所有到山脚的距离
        # 状态转移方程，如果元素单调递增则有left[i] = left[i - 1] + 1,否则为0
        for i in range(1, n):
            left[i] = (left[i - 1] + 1 if A[i - 1] < A[i] else 0)
        right = [0] * n
        # 右边元素同理。依旧使用动态规划算出所有到山脚的距离
        for i in range(n - 2, -1, -1):
            right[i] = (right[i + 1] + 1 if A[i + 1] < A[i] else 0)
        res = 0
        # 如果两面的距离都大于0，证明有一段山巅，这时候算出距离，取所有距离的最大值
        for i in range(n):
            if left[i] > 0 and right[i] > 0:
                res = max(res, left[i] + right[i] + 1)
        return res

