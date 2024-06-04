'''
coding:utf8
@Time : 2020/2/14 19:11
@Author : cjr
@File : 最长公共前缀.py
题目链接：https://leetcode-cn.com/problems/longest-common-prefix/
'''


class Solution:
    """
    1、本题目求最长公共前缀，我们可以采用字符串A和B相比较求出最长前缀，再与C比较
    以此类推，求出最终的最长前缀
    2、现在问题变成了求两个字符串的最长公共前缀，这样如果我们从第一个字符开始比较
    的话，与C比较时候会再次从第一个字符比较增加不必要的开销，所以我们选择整体比较，
    如果整体不同则去掉末尾一个字符。
    """
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        # 初始化第一个字符串
        s = strs[0]
        # 因为比较的字符串不包括第一个已经初始化好的，所以比较需要从第二个开始也就是1
        for i in range(1, len(strs)):
            # 如果在B串中找不到A串，则末尾去掉一个，再检测，用while循环可以直到A和B完全相等再结束循环
            while strs[i].find(s) != 0:
                s = s[:-1]
        return s

