"""
coding: utf8
@time: 2020/12/15 14:13
@author: cjr
@file: 并查集模板.py
"""
################################
# 并查集模板
################################


class CheckAndSet:
    def __init__(self, n):
        self.p = [i for i in range(n)]

    def union(self, i, j):
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


