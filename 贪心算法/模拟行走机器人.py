"""
coding: utf8
@time: 2020/11/23 23:47
@author: cjr
@file: 模拟行走机器人.py
题目链接：https://leetcode-cn.com/problems/walking-robot-simulation/
"""
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        res = 0
        dic = {
            'up': [0, 1, 'left', 'right'],
            'down': [0, -1, 'right', 'left'],
            'left': [-1, 0, 'down', 'right'],
            'right': [1, 0, 'up', 'down']
        }
        x, y = 0, 0
        dir1 = 'up'
        obstacles = set(map(tuple, obstacles))
        for command in commands:
            if command > 0:
                for i in range(command):
                    if (x + dic[dir1][0], y + dic[dir1][1]) not in obstacles:
                        x += dic[dir1][0]
                        y += dic[dir1][1]
                        res = max(x ** 2 + y ** 2, res)
                    else:
                        break
            else:
                if command == -1:
                    dir1 = dic[dir1][3]
                else:
                    dir1 = dic[dir1][2]
        return res



