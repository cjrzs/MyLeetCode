'''
coding:utf8
@Time : 2020/3/15 22:06
@Author : cjr
@File : 爬楼梯.py
题目链接：https://leetcode-cn.com/problems/climbing-stairs/
'''


class Solution:
    """
    其实就是斐波那契数列的应用。
    首先n=1时候有一种方法。n=2时候有两种方法，
    以此类推，n可以转换成n-1和n-2之和，
    即：f(n) = f(n-1) + f(n-2)
    其实简单理解就是从第三个数开始，第三个数等于前两个数之和！！！
    """
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n-1):
            a, b = a+b, a
        return a


