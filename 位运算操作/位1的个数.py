"""
coding: utf8
@time: 2020/12/9 22:42
@author: cjr
@file: 位1的个数.py
题目链接:https://leetcode-cn.com/problems/number-of-1-bits/
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # n & (n - 1) 这个操作 可以使n每次去掉一个1.
            n = n & (n - 1)
            count += 1
        return count

