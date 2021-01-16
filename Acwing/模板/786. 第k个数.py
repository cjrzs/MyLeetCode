"""
coding: utf8
@time: 2021/1/16 18:49
@author: cjr
@file: 786. 第k个数.py
给定一个长度为n的整数数列，以及一个整数k，请用快速选择算法求出数列从小到大排序后的第k个数。

输入格式
第一行包含两个整数 n 和 k。

第二行包含 n 个整数（所有整数均在1~109范围内），表示整数数列。

输出格式
输出一个整数，表示数列的第k小数。

数据范围
1≤n≤100000,
1≤k≤n
输入样例：
5 3
2 4 1 5 3
输出样例：
3
"""


def quick(nums, l, r, k):
    if l >= r:
        return

    x, i, j = nums[l], l - 1, r + 1
    while i < j:
        while True:
            i += 1
            if nums[i] >= x:
                break
        while True:
            j -= 1
            if nums[j] <= x:
                break
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    # sl = j - l + 1
    # 对于区间的划分是 左面是[l, j] 右面是[j + 1, r]
    # 所以当 k 小于 j + 1 时候答案一定在左面，反之在右面
    if j < k - 1:
        quick(nums, j + 1, r, k)
    else:
        quick(nums, l, j, k)


n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
quick(nums, 0, n - 1, k)
print(nums[k - 1])




