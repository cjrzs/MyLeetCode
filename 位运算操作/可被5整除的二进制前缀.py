"""
coding: utf8
@time: 2021/1/14 22:33
@author: cjr
@file: 可被5整除的二进制前缀.py
题目链接:https://leetcode-cn.com/problems/binary-prefix-divisible-by-5/
"""
from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        """
        这里有一个技巧：因为是只需要判断能否被五整除
        只需要记余数就可以
        :param A:
        :return:
        """
        pre = 0
        res = []
        for item in A:
            pre = ((pre << 1) + item) % 5
            res.append(pre == 0)
        return res


