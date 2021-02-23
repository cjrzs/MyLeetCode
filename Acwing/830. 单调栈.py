"""
coding: utf8
@time: 2021/1/25 0:11
@author: cjr
@file: 830. 单调栈.py
给定一个长度为N的整数数列，输出每个数左边第一个比它小的数，如果不存在则输出-1。

输入格式
第一行包含整数N，表示数列长度。

第二行包含N个整数，表示整数数列。

输出格式
共一行，包含N个整数，其中第i个数表示第i个数的左边第一个比它小的数，如果不存在则输出-1。

数据范围
1≤N≤105
1≤数列中元素≤109
输入样例：
5
3 4 2 7 5
输出样例：
-1 3 -1 2 2
"""

# 主要思想就是，依次求每个元素的前面第一个比它小的元素
# 那么只要保证栈（tmp）中的元素是单调递增的，那么栈顶（tmp[-1]）的元素就是第一个比当前元素小的
# 我们如何保证单调性呢？ 我们可以再循环中把所有扰乱单调性的元素全部pop。

n = int(input())
nums = list(map(int, input().split()))

res, tmp = [], []
for i in range(n):
    while tmp and tmp[-1] >= nums[i]:
        tmp.pop()
    res.append(tmp[-1] if tmp else -1)
    tmp.append(nums[i])

print(' '.join(map(str, res)))




