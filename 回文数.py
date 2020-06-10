'''
coding=utf8
@Time: 2020/1/18
@Author: cjr
@File: 回文数
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
'''


class Solution:

    def isPalindrome(self, x: int) -> bool:
        """
        思路是设置一个为0的整数tmp，输入的数（x）取余拿到末尾数
        tmp*10拿到首位数字加上末尾数得到新的tmp的第一个数
        以此类推完整的倒序整个输入的x。
        需要注意的有两点
        1、每次过后x必须除以10再取整，保证每次都取到的是最后一位数字
        2、必须要把x备份一下，否则过程中因为除以10了，x的结果会变成0
        :param x:
        :return:
        """
        temp = 0
        y = x
        if x < 0:
            return False
        elif x == 0:
            return True
        elif x > 0:
            while x:
                temp = temp*10 + x % 10
                x = int(x/10)
            if temp == y:
                return True
            else:
                return False

    def isPalindrome2(self, x: int) -> bool:
        """
        2020年6月10号，今天的每日一题
        与上次做这道题的时间时隔了五个月，终于在只看了一眼提示的情况下做了出来，呜呜呜~~~
        :param x:
        :return:
        """
        new_x = x
        res = 0
        if x < 0:
            return False
        while new_x >= 1:
            a = new_x % 10
            res = res * 10 + a
            new_x = new_x // 10
        return x == res
