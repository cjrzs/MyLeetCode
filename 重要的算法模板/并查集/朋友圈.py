"""
coding: utf8
@time: 2020/12/15 12:54
@author: cjr
@file: 朋友圈.py
题目链接：https://leetcode-cn.com/problems/friend-circles/
"""
from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        n = len(M)
        p = [i for i in range(n)]
        for i in range(n):
            for j in range(n):
                if M[i][j]:
                    self._union(p, i, j)
        return len(set(self._parent(p, i) for i in range(n)))

    def _union(self, p, i, j):
        p1 = self._parent(p, i)
        p2 = self._parent(p, j)
        p[p1] = p2

    @staticmethod
    def _parent(p, i):
        """
        找到头元素
        :param p:
        :param i:
        :return:
        """
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            x = i
            i = p[i]
            p[x] = root
        return root

