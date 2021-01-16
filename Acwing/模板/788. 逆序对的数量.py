"""
coding: utf8
@time: 2021/1/16 23:35
@author: cjr
@file: 788. 逆序对的数量.py
给定一个长度为n的整数数列，请你计算数列中的逆序对的数量。

逆序对的定义如下：对于数列的第 i 个和第 j 个元素，如果满足 i < j 且 a[i] > a[j]，则其为一个逆序对；否则不是。

输入格式
第一行包含整数n，表示数列的长度。

第二行包含 n 个整数，表示整个数列。

输出格式
输出一个整数，表示逆序对的个数。

数据范围
1≤n≤100000
输入样例：
6
2 3 4 5 6 1
输出样例：
5
"""

n = int(input())
nums = list(map(int, input().split()))

res = 0


def merge(nums, l, r):
    if l >= r:
        return 0
    mid = (l + r) >> 1
    res = merge(nums, l, mid) + merge(nums, mid + 1, r)
    i, j = l, mid + 1
    tmp = []

    while i <= mid and j <= r:
        if nums[i] <= nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            res += mid - i + 1
            tmp.append(nums[j])
            j += 1
    while i <= mid:
        tmp.append(nums[i])
        i += 1
    while j <= r:
        tmp.append(nums[j])
        j += 1
    for idx, i in enumerate(tmp):
        nums[idx + l] = i
    return res


print(merge(nums, 0, n - 1))





