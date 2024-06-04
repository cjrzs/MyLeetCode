"""
coding:utf8
@Time : 2020/8/20 23:13
@Author : cjr
@File : 扫雷游戏.py
题目链接：https://leetcode-cn.com/problems/minesweeper/
"""
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':  # 踩到了地雷，直接更新并返回
            board[click[0]][click[1]] = 'X'
            return board
        if board[click[0]][click[1]].isdigit():  # 踩到了走过的位置，直接返回
            return board
        global a,b
        a,b,m,n = [-1,1,0,0,-1,-1,1,1],[0,0,-1,1,-1,1,-1,1],len(board),len(board[0])
        def dfs(x,y):
            # 首先判断其周围是否有没有地 雷，
            count = 0
            for i in range(8):
                if x+a[i]>=0 and x+a[i]<m and y+b[i]>=0 and y+b[i]<n and board[x+a[i]][y+b[i]]=='M':
                    count+=1
            if count:# 如果有地 雷的话，计算地 雷的数量，返回
                board[x][y] = str(count)
            else:    # 如果没有地 雷的话，对每一个周围的满足条件的位置进行递归
                board[x][y] = 'B'
                for i in range(8):
                    if x+a[i]>=0 and x+a[i]<m and y+b[i]>=0 and y+b[i]<n and  board[x+a[i]][y+b[i]]=='E':
                        dfs(x+a[i],y+b[i])
        dfs(click[0],click[1])
        return board


