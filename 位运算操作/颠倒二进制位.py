"""
coding: utf8
@time: 2020/12/10 11:16
@author: cjr
@file: 颠倒二进制位.py
题目链接：https://leetcode-cn.com/problems/reverse-bits/
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(31, -1, -1):
            # 取最后一位左移i位
            tmp = (n & 1) << i
            # 加到结果
            res += tmp
            # 然后最后一位右移一位，即更新最后一位的位置
            n >>= 1
        return res

