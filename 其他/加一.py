'''
coding:utf8
@Time : 2020/3/6 0:01
@Author : cjr
@File : 加一.py
题目链接：https://leetcode-cn.com/problems/plus-one/
'''


class Solution:
    """
    第一种方法，列表转字符串转数字再加一之后转回去，不多说，属于取巧，偏离本题考的目的
    下面说下我的题解。
    首先定义个标志i=0，这个是列表中9的个数。
    while循环列表长度，当最后一个数字是9，把他变成0，然后标志位+1，如果不是终止循环
    下面一步用当前i的值和输入的列表长度比较，如果相等说明列表中全部是9，那么我们在列表最前面添加一个1
    如果不是我们则在第一个不是9的位置+1
    """
    def plusOne(self, digits: list) -> list:
        i = 0
        while i < len(digits):
            if digits[len(digits)-i-1] == 9:
                digits[len(digits) - i - 1] = 0
                i += 1
            else:
                break
        if i == len(digits):
            digits.insert(0, 1)
        else:
            digits[len(digits) - i - 1] += 1
        return digits

