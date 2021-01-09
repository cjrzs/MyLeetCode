"""
coding: utf8
@time: 2021/1/9 22:48
@author: cjr
@file: 895. 最长上升子序列.py
"""
"""
给定一个长度为N的数列，求数值严格单调递增的子序列的长度最长是多少。

输入格式
第一行包含整数N。

第二行包含N个整数，表示完整序列。

输出格式
输出一个整数，表示最大长度。

数据范围
1≤N≤1000，
−109≤数列中的数≤109
输入样例：
7
3 1 2 1 8 5 6
输出样例：
4
"""


def zixulie(L):
    dp = [1] * len(L)
    for i in range(len(L)):
        for j in range(i):
            if L[j] < L[i]:
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp)


if __name__ == '__main__':
    N = int(input())

    L = [int(i) for i in input().split(' ')]
    print(zixulie(L))







