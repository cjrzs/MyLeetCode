"""
coding: utf8
@time: 2020/10/31 11:36
@author: cjr
@file: 有效的字母异位词.py
题目链接：https://leetcode-cn.com/problems/valid-anagram/description/
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        使用哈希表计算次数。
        :param s:
        :param t:
        :return:
        """
        tmp = {}
        for i in range(len(s)):
            if s[i] not in tmp:
                tmp[s[i]] = 1
            else:
                tmp[s[i]] += 1
        arr = [0] * len(tmp)
        for i in range(len(t)):
            if t[i] not in tmp:
                return False
            else:
                tmp[t[i]] -= 1
        return arr == tmp.values()

    def isAnagram(self, s: str, t: str) -> bool:
        """
        排序看是否相等即可。
        :param s:
        :param t:
        :return:
        """
        s = sorted(s)
        t = sorted(t)
        return s == t
