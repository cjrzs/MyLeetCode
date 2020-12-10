"""
coding: utf8
@time: 2020/12/10 16:47
@author: cjr
@file: N皇后2.py
题目链接：https://leetcode-cn.com/problems/n-queens/
"""
from typing import List, Union


#################################
# N皇后的最终解决方案（位运算）
#################################


class Solution:
    def __init__(self):
        self.count = 0

    def solveNQueens(self, n: int) -> Union[list, int]:
        if n == 0:
            return 0
        self.dfs(n, 0, 0, 0, 0)
        return self.count

    def dfs(self, n, row, col, pie, na):
        if row >= n:
            self.count += 1
            return
        bits = (~(col | pie | na)) & ((1 << n) - 1)
        while bits:
            p = bits & -bits
            bits = bits & (bits - 1)
            self.dfs(n, row + 1, col | p, (pie | p) << 1, (na | p) >> 1)

