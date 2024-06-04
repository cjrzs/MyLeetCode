"""
coding: utf8
@time: 2020/11/22 11:26
@author: cjr
@file: 岛屿数量.py
题目链接：https://leetcode-cn.com/problems/number-of-islands/
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        count = 0

        # dfs把 ‘1’ 周围的岛屿都变成 ‘0’，因为他们会连城一个整体，计数都为1个岛
        def dfs(i, j):
            # 结束条件i，j超出边界，或者直接就是 ‘0’
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        # 遍历整个网格，如果是 ‘1’， 计数就+1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count

