"""
coding: utf8
@time: 2021/1/16 16:00
@author: cjr
@file: binary_search.py
给定一个按照升序排列的长度为n的整数数组，以及 q 个查询。

对于每个查询，返回一个元素k的起始位置和终止位置（位置从0开始计数）。

如果数组中不存在该元素，则返回“-1 -1”。

输入格式
第一行包含整数n和q，表示数组长度和询问个数。

第二行包含n个整数（均在1~10000范围内），表示完整数组。

接下来q行，每行包含一个整数k，表示一个询问元素。

输出格式
共q行，每行包含两个整数，表示所求元素的起始位置和终止位置。

如果数组中不存在该元素，则返回“-1 -1”。

数据范围
1≤n≤100000
1≤q≤10000
1≤k≤10000
输入样例：
6 3
1 2 2 3 3 4
3
4
5
输出样例：
3 4
5 5
-1 -1
"""


def b_search(nums, x):
    n = len(nums)
    l, r = 0, n - 1
    while l < r:
        mid = (l + r) >> 1
        if nums[mid] >= x:
            r = mid
        else:
            l = mid + 1
    if nums[l] != x:
        return ['-1', '-1']
    else:
        res = str(l)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r + 1) >> 1
            if nums[mid] <= x:
                l = mid
            else:
                r = mid - 1
    return [str(res), str(l)]


n, q = list(map(int, input().split()))
nums = list(map(int, input().split()))
qq = []
res = ''
for _ in range(q):
    qq.append(int(input()))
for target in qq:
    res += ' '.join(b_search(nums, target))
print(res.rstrip())












