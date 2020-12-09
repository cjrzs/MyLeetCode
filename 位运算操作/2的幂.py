"""
coding: utf8
@time: 2020/12/9 23:24
@author: cjr
@file: 2的幂.py
题目链接：https://leetcode-cn.com/problems/power-of-two/
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        本题有一个知识就是如果是2的幂，那么这个数字的二进制 有且只有一个1，
        就是计算二进制时候到最后那个 1 % 2 == 1. 其他时候都应整数余数为0
        :param n:
        :return:
        """
        # 所以我们在这里只要把最后一个1 减去剩下的数就应该等于0
        return n != 0 and (n & (n - 1)) == 0

