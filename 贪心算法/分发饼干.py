"""
coding: utf8
@time: 2020/11/23 14:43
@author: cjr
@file: 分发饼干.py
题目链接：https://leetcode-cn.com/problems/assign-cookies/
"""
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        先排序，因为每个孩子只能要一个饼干，所以只要饼干能符合孩子胃口就 + 1，表示满足了一个孩子
        :param g:
        :param s:
        :return:
        """
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i
