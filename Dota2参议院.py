"""
coding: utf8
@time: 2020/12/11 23:27
@author: cjr
@file: Dota2参议院.py
题目链接：https://leetcode-cn.com/problems/dota2-senate/
"""
import collections


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = collections.deque()
        dire = collections.deque()
        for i, val in enumerate(senate):
            if val == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)
            radiant.popleft()
            dire.popleft()
        return 'Radiant' if radiant else 'Dire'
