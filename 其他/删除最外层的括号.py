"""
coding: utf8
@time: 2020/10/28 23:07
@author: cjr
@file: 删除最外层的括号.py
题目链接：https://leetcode-cn.com/problems/remove-outermost-parentheses/
"""


class Solution:

    def removeOuterParentheses(self, S: str) -> str:
        """
        遇到左括号计数就+1，右括号就-1
        计数到0了，说明遇到了最外层括号
        这时候直接把分片放在结果数组里
        拼接最后的数组就行了
        :param S:
        :return:
        """
        n = 0
        res = []
        left = 0
        for i in range(len(S)):
            if S[i] == '(':
                n += 1
            else:
                n -= 1
            if n == 0:
                # 因为最外层的括号要去掉所以left要+1
                res.append(S[left+1: i])
                # 跳过最外层的右括号，指针指向下一个左括号
                left = i + 1
        return ''.join(res)
