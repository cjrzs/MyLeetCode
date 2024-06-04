"""
coding: utf8
@time: 2020/10/24 22:23
@author: cjr
@file: 猜数字游戏.py
题目链接：https://leetcode-cn.com/problems/bulls-and-cows/submissions/
"""
from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """
        用字典记录位置，处理过的都换成其他字符
        时间复杂度： O(n^2) 最后锁定处理过的奶牛时候又遍历了一遍
        :param secret:
        :param guess:
        :return:
        """
        sec_d = {}
        gue_d = {}
        for i in range(len(secret)):
            sec_d[i] = secret[i]
        for i in range(len(guess)):
            gue_d[i] = guess[i]
        index = 0
        x = 0
        y = 0
        while index < len(guess):
            if sec_d[index] == gue_d[index]:
                x += 1
                gue_d[index] = 'z'
                sec_d[index] = 'y'
            index += 1
        index2 = 0
        while index2 < len(gue_d):
            if sec_d[index2] in gue_d.values():
                y += 1
                ks = [k for k, v in gue_d.items() if v == sec_d[index2]]
                gue_d[ks[0]] = 'x'
            index2 += 1
        return f'{x}A{y}B'

    def getHint2(self, secret: str, guess: str) -> str:
        """
        用数组记录位置，处理过的都换成其他字符
        时间复杂度: O(n)
        :param secret:
        :param guess:
        :return:
        """
        A, B = 0, 0
        S, G = [], []
        for i, con in enumerate(guess):
            if con == secret[i]:
                A += 1
            else:
                S.append(secret[i])
                G.append(guess[i])
        for i in S:
            if i in G:
                B += 1
                G[G.index(i)] = 'x'
        return f'{A}A{B}B'


