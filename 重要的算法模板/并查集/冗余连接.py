"""
coding: utf8
@time: 2020/12/15 22:06
@author: cjr
@file: 冗余连接.py
题目链接：https://leetcode-cn.com/problems/redundant-connection/
"""
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        p = [i for i in range(n + 1)]
        for x, y in edges:
            if self.union(p, x, y):
                return [x, y]

    @staticmethod
    def find(p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            tmp = i
            i = p[i]
            p[tmp] = root
        return root

    def union(self, p, i, j):
        p1 = self.find(p, i)
        p2 = self.find(p, j)
        p[p1] = p2
        return p1 == p2


