'''
@Time: 2020/1/12
@Author: cjr
@File: 整数翻转
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
'''


class Solution:

    def reverse(self, x: int) -> int:
        """
        暴力思路，直接用切片进行字符串翻转，对结果进行判断
        :param x:
        :return: 翻转后范围（-2147483648~2147483647）
        """
        str_int = str(x)
        if str_int[0] == "-":
            result = -int(str_int[:0:-1])
        else:
            result = int(str_int[::-1])
        return result if -2147483648 < result < 2147483647 else 0
