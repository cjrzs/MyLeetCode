"""
coding:utf8
@Time : 2020/8/13 12:12 
@Author : CJR  
@File : 字符串相乘.py
题目链接：https://leetcode-cn.com/problems/multiply-strings/
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        # 初始化结果数组，根据竖式相乘规律可知长度为两个字符串相加-1
        # （PS：难以理解，可以用几个例子试一试）
        res = [0 for _ in range(len(num1) + len(num2) - 1)]
        # 第二个字符串倒序，是因为需要从个位数开始相乘
        for i in range(len(num1)):
            for j in range(len(num2)-1, -1, -1):
                # 因为i+j位上根据字符串长度不同会有多个值，该位上的结果需要把他们都加起来
                res[i+j] += (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
        # 对结果数组进行进位
        for k in range(len(res)-1, 0, -1):
            res[k-1] += res[k] // 10
            res[k] %= 10
        return ''.join(map(str,res))
