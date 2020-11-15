"""
coding: utf8
@time: 2020/11/15 12:17
@author: cjr
@file: 移掉K位数字.py
题目链接：https://leetcode-cn.com/problems/remove-k-digits/
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        本题需要知道在什么情况下可以删掉元素
        从左往右遍历的时候，当前元素比前一个元素小的时候，删除掉前一个会使整体变最小！
        :param num:
        :param k:
        :return:
        """
        end = len(num) - k
        stack = []
        for n in num:
            # 判断当前元素是否小于前一个元素。如果小于就把栈中最后一位出栈，直到K等于0或者栈空
            while k and stack and n < stack[-1]:
                stack.pop()
                k -= 1
            # 每个元素都入栈
            stack.append(n)
        # 最后结果直接返回栈中元素去掉K的长度，防止单调栈的情况
        return ''.join(stack[: end]).lstrip('0') or '0'
