"""
coding: utf8
@time: 2021/1/23 15:15
@author: cjr
@file: 801. 二进制中1的个数.py
给定一个长度为n的数列，请你求出数列中每个数的二进制表示中1的个数。

输入格式
第一行包含整数n。

第二行包含n个整数，表示整个数列。

输出格式
共一行，包含n个整数，其中的第 i 个数表示数列中的第 i 个数的二进制表示中1的个数。

数据范围
1≤n≤100000,
0≤数列中元素的值≤109
输入样例：
5
1 2 3 4 5
输出样例：
1 1 2 1 2
"""


n = int(input())
nums = list(map(int, input().split()))


# 计算最后一个1
def low_bit(x):
    return x & -x


for i in range(n):
    cur = nums[i]
    res = 0
    # 如果当前输入的数字不为0的话，就循环
    while cur:
        # 每循环一次结果 +1
        # 每次在当前基础上减去最后一个1，这样减到0，就统计出了1的数量
        res += 1
        cur -= low_bit(cur)
    print(res, end=' ')



