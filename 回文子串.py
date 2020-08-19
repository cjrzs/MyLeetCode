"""
coding:utf8
@Time : 2020/8/19 23:53
@Author : cjr
@File : 回文子串.py
题目链接：https://leetcode-cn.com/problems/palindromic-substrings/
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        中心扩展，因为是回文串，所以从中间开始向两边检测
        遇到回文串计数+1
        （PS：需要举例理解）
        时空复杂度： O(n^2), O(1)
        :param s:
        :return:
        """
        n = len(s)
        # 设置个res用来计数
        self.res = 0

        # 给出两个中间值开始向两侧扩展，遇到回文计数则+1
        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
                self.res += 1
        # 字符串个数奇数和偶数时应该用不同的处理
        # （这里不会重复检测，因为奇数时是从一个字符向两侧扩展，偶数时两个字符同时扩展）
        for i in range(n):
            helper(i, i)
            helper(i, i + 1)
        return self.res


