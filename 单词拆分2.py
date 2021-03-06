"""
coding: utf8
@time: 2020/11/1 20:05
@author: cjr
@file: 单词拆分2.py
题目链接：https://leetcode-cn.com/problems/word-break-ii/
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        回溯，找出所有组合
        备忘录，跳过已经搜索过的组合。
        :param s:
        :param wordDict:
        :return:
        """
        res = []
        mome = [1] * (len(s)+1)
        wordDict = set(wordDict)

        def dfs(wordDict, tmp, pos):
            num = len(res)
            if pos == len(s):
                res.append(' '.join(tmp))
                return
            for i in range(pos, len(s) + 1):
                if mome[i] and s[pos: i] in wordDict:
                    tmp.append(s[pos: i])
                    dfs(wordDict, tmp, i)
                    tmp.pop()
            mome[pos] = 1 if len(res) > num else 0
        dfs(wordDict, [], 0)
        return res
