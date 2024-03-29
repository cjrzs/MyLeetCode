"""
coding: utf8
@time: 2021/3/11 23:04
@author: cjr
@file: 基本计算器 II.py

给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

整数除法仅保留整数部分。



示例 1：
输入：s = "3+2*2"
输出：7
示例 2：

输入：s = " 3/2 "
输出：1
示例 3：

输入：s = " 3+5 / 2 "
输出：5


提示：
1 <= s.length <= 3 * 105
s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
s 表示一个 有效表达式
表达式中的所有整数都是非负整数，且在范围 [0, 231 - 1] 内
题目数据保证答案是一个 32-bit 整数
"""


class Solution:
    """
    思路：使用栈存储当前的数字，并在遇到乘法或者除法的时候弹出栈顶元素与当前元素计算。
         最后计算栈中所有数字之和。
    1. 遇到数字开始计算当前数字。
    2. 遍历到最后一个字符 or 遇到加减乘除 进入第二阶段
        a. 上一个符号是“+”，将当前数入栈。
        b. 上一个符号是“-”，将当前数的负数入栈。
        c. 上一个符号是“*”，将栈顶元素出栈与当前数字计算乘法，并将结果入栈
        d. 上一个符号是“/”，将栈顶元素出栈与当前数字计算除法，并将结果入栈
        （ps：每次计算后更新当前数字，更新符号为当前符号）
        最后，可以看到我们是根据上一个符号来进行计算的，所以当遍历到最后一个字符的时候
        还应该进行一次运算，把当前字符和当前符号计算一下。否则会少运算一次。
    3. 此时栈中的乘除已经计算好结果了，并且负数前面也带上了负号，只要把栈中元素全相加即可。
    """
    def calculate(self, s: str) -> int:
        num, sign, stack = 0, '+', []
        for i, c in enumerate(s):
            c: str
            if c.isdigit():
                # 计算当前数字
                num = num * 10 + int(c)
            # 这里不能用elif，否则走不到i == len(s) - 1这个条件（别问我为啥知道，呜呜~~~~）。
            if i == len(s) - 1 or c in '+-*/':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = c
        return sum(stack)

















