"""
coding: utf8
@time: 2021/1/11 17:02
@author: cjr
@file: 省份数量.py
题目链接：https://leetcode-cn.com/problems/number-of-provinces/submissions/
"""
from typing import List


class CS:

    def __init__(self, x):
        self.p = x

    def find(self, i, j):
        p1 = self.parent(i)
        p2 = self.parent(j)
        self.p[p1] = p2

    def parent(self, i):
        root = i
        while self.p[root] != root:
            root = self.p[root]
        while self.p[i] != i:
            tmp = i
            i = self.p[i]
            self.p[tmp] = root
        return root


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        x = [i for i in range(n)]
        cs = CS(x)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    cs.find(i, j)
        res = sum(x[i] == i for i in range(n))
        return res

