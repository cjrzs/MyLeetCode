'''
coding:utf8
@Time : 2020/7/8 22:32
@Author : cjr
@File : 跳水板.py
题目链接：https://leetcode-cn.com/problems/diving-board-lcci/
'''
from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if shorter == longer:
            return [k*shorter]
        dp = [0] * (k + 1)
        dp[0] = shorter * k
        for i in range(1, k + 1):
            dp[i] = dp[i - 1] + longer - shorter
        return dp

