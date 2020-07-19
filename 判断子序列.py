'''
coding:utf8
@Time : 2020/7/19 17:04
@Author : cjr
@File : 判断子序列.py
题目链接：https://leetcode-cn.com/problems/is-subsequence/
'''


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        双指针：
        两个指针从0开始遍历两个字符串
        如果两个指针的值相等两个指针均后移
        如果不相等s的指针原地等待匹配，t的指针后移
        最后判断s的指针与s的字符串长度是否相等。
        :param s:
        :param t:
        :return:
        """
        i = j = 0
        n, m = len(t), len(s)
        while i < n and j < m:
            if t[i] == s[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == m

