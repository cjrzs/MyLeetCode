"""
coding: utf8
@time: 2020/10/20 21:31
@author: cjr
@file: 两个相同字符之间的最长子字符串.py
题目链接：https://leetcode-cn.com/problems/largest-substring-between-two-equal-characters/submissions/
"""


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """
        害，比赛直接暴力法得了
        两重循环遇见相等的字符串就把它们的长度存起来，最后比较最长的就可以了
        时间复杂度 O(n^2)
        :param s:
        :return:
        """
        res = []
        for i in range(len(s) - 1):
            for j in range(len(s) - 1, i, -1):
                if s[i] == s[j]:
                    res.append(len(s[i + 1: j]))
        return max(res) if res else -1

    def maxLengthBetweenEqualCharacters2(self, s: str) -> int:
        """
        用一个字典存第一次出现的下标和值
        并且当后续出现字典中值时候计算距离，取最大的距离
        时间复杂度 O(n) ,只需要一次遍历
        :param s:
        :return:
        """
        left, right, res = {}, {}, -1
        for i, v in enumerate(s):
            if v not in left:
                left[v] = i
            else:
                res = max(res, i - left[v] - 1)
        return res
