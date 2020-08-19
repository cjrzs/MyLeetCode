"""
coding:utf8
@Time : 2020/8/11 12:16 
@Author : CJR  
@File : 被围绕的区域.py
题目链接：https://leetcode-cn.com/problems/surrounded-regions/
"""
from typing import List


class Solution:
    """
    由于题目太难本人不会，只能copy一波官方题解了
    """
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 如果数组长或宽小于等于2，则不需要替换
        if len(board) <= 2 or len(board[0]) <= 2:
            return

        row, col = len(board), len(board[0])

        def dfs(i, j):
            """
            深度优先算法，如果符合条件，替换为A并进一步测试，否则停止
            把所有的O都替换成A
            条件1：必须是'O'才可以更改
            条件2：需要在图内
            """
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != 'O':
                return
            board[i][j] = 'A'

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        # 从外围开始
        for i in range(row):
            dfs(i, 0)
            dfs(i, col - 1)

        for j in range(col):
            dfs(0, j)
            dfs(row - 1, j)

        # 最后完成替换
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'

