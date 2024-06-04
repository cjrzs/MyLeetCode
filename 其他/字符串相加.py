"""
coding:utf8
@Time : 2020/8/3 11:07 
@Author : CJR  
@File : 字符串相加.py
题目链接：https://leetcode-cn.com/problems/add-strings/
"""


class Solution:

    def add_strings(self, num1: str, num2: str) -> str:
        """
        竖式逐位相加
        该算法巧妙的地方在于，当两个字符串长度不一样的时候，使用0补全。
        时间复杂度：O(max(len(num1), len(num2)))，逐位相加，取最长字符串的长度
        空间复杂度：O(1)，双指针，没有使用到额外空间。
        :param num1:
        :param num2:
        :return:
        """
        # 初始化空字符串保存结果
        res = ''
        # 竖式运算从末尾开始相加
        point1, point2, carry = len(num1) - 1, len(num2) - 1, 0
        # 只有当两个字符串全部走到末尾才可以结束运算
        while point1 >= 0 or point2 >= 0:
            # 当两个字符串有长度差的时候，使用0去计算缺失的位置
            n1 = int(num1[point1]) if point1 >= 0 else 0
            n2 = int(num2[point2]) if point2 >= 0 else 0
            # 临时存储当前位置两个字符串中字符相加再加上进位的结果
            tmp = n1 + n2 + carry
            # carry表示进位
            carry = tmp // 10
            # 当前应该存储到res的结果
            curr = tmp % 10
            # 存储结果
            res = str(curr) + res
            #　指针前移，选取下一个元素
            point1, point2 = point1 - 1, point2 - 1
        # 最后结果,如果有进位需要 + 1
        return '1' + res if carry else res
