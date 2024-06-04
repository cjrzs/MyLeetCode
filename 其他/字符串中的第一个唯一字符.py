"""
coding: utf8
@time: 2020/12/24 0:31
@author: cjr
@file: 字符串中的第一个唯一字符.py
题目链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string/
"""
import collections


class Solution:
    def firstUniqhar(self, s: str) -> int:
        if not s:
            return -1
        counts = collections.Counter(s)
        for val, idx in counts.items():
            if idx == 1:
                return s.index(val)
        return -1

