"""
coding:utf8
@Time : 2020/7/30 12:00 
@Author : CJR  
@File : 整数拆分.py
题目链接：https://leetcode-cn.com/problems/integer-break/
"""
class Solution:
    """
    还可以使用动态规划。
    """
    def integerBreak(self, n: int) -> int:
        """
        数学方法。
        时/空复杂度：都是O(1) 只涉及到数学运算
        :param n:
        :return:
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        tmp1 = n // 3
        tmp2 = n % 3
        if tmp2 == 0:
            result = 3 ** tmp1
        elif tmp2 == 1:
            result = 3 ** (tmp1 - 1) * 4
        elif tmp2 == 2:
            result = 3 ** tmp1 * 2
        return result


