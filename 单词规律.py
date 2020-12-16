"""
coding: utf8
@time: 2020/12/16 11:02
@author: cjr
@file: 单词规律.py
题目链接：https://leetcode-cn.com/problems/word-pattern/
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        visited = set()
        s_array = s.split(' ')
        for i in range(len(pattern)):
            if pattern[i] in dic:
                if dic[pattern[i]] != s_array[i]:
                    return False
            else:
                if s_array[i] in visited:
                    return False
                dic[pattern[i]] = s_array[i]
                visited.add(s_array[i])
        return True




