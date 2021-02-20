"""
coding: utf8
@time: 2021/1/23 13:16
@author: cjr
@file: 799. 最长连续不重复子序列.py
给定一个长度为n的整数序列，请找出最长的不包含重复的数的连续区间，输出它的长度。

输入格式
第一行包含整数n。

第二行包含n个整数（均在0~100000范围内），表示整数序列。

输出格式
共一行，包含一个整数，表示最长的不包含重复的数的连续区间的长度。

数据范围
1≤n≤100000
输入样例：
5
1 2 2 3 5
输出样例：
3
"""
# 使用双指针解决

n = int(input())
nums = list(map(int, input().split()))

# count是一个计数数组，统计每个字符出现的数量
count = [0] * (n + 1)
res, j = 0, 0
for i in range(n):
    # 统计每个字符出现的次数
    count[nums[i]] += 1
    # 如果一个字符连续出现了两次，并且j还在i的前面移动j
    while count[nums[i]] >= 2 and i >= j:
        # 移动j的同时要减少统计过字符的数量。
        count[nums[j]] -= 1
        j += 1
    # 每次移动i都统计当前的长度
    res = max(res, i - j + 1)
print(res)

enumerate


