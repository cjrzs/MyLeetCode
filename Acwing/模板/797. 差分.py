"""
coding: utf8
@time: 2021/1/20 23:09
@author: cjr
@file: 797. 差分.py
输入一个长度为n的整数序列。

接下来输入m个操作，每个操作包含三个整数l, r, c，表示将序列中[l, r]之间的每个数加上c。

请你输出进行完所有操作后的序列。

输入格式
第一行包含两个整数n和m。

第二行包含n个整数，表示整数序列。

接下来m行，每行包含三个整数l，r，c，表示一个操作。

输出格式
共一行，包含n个整数，表示最终序列。

数据范围
1≤n,m≤100000,
1≤l≤r≤n,
−1000≤c≤1000,
−1000≤整数序列中元素的值≤1000
输入样例：
6 3
1 2 2 1 2 1
1 3 1
3 5 1
1 6 1
输出样例：
3 4 5 3 4 2
"""
n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))

b = [0] * (n + 10)


def insert(l, r, c):
    b[l] += c
    b[r + 1] -= c


# 这里要初始化b数组
for i in range(1, n + 1):
    insert(i, i, nums[i])


while m:
    m -= 1
    l, r, c = map(int, input().split())
    insert(l, r, c)

for i in range(1, n + 1):
    b[i] += b[i - 1]
    print(b[i], end=' ')




