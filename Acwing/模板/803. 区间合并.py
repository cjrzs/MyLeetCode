"""
coding: utf8
@time: 2021/1/23 23:22
@author: cjr
@file: 803. 区间合并.py
给定 n 个区间 [li,ri]，要求合并所有有交集的区间。

注意如果在端点处相交，也算有交集。

输出合并完成后的区间个数。

例如：[1,3]和[2,6]可以合并为一个区间[1,6]。

输入格式
第一行包含整数n。

接下来n行，每行包含两个整数 l 和 r。

输出格式
共一行，包含一个整数，表示合并区间完成后的区间个数。

数据范围
1≤n≤100000,
−109≤li≤ri≤109
输入样例：
5
1 2
2 4
5 6
7 8
7 9
输出样例：
3
"""
# 读入
n = int(input())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))

# 先按照区间第一个元素排序
nums.sort(key=lambda x: x[0])
cur = [-float('inf'), -float('inf')]

# 遍历
res = []
for num in nums:
    # 如果nums中区间的第一个元素，比当前区间的最后一个元素还要大，那么说明区间无相交
    if num[0] > cur[1]:
        # 必须不是第一个虚拟区间才可以放到结果里
        if cur[1] != -float('inf'):
            res.append(num)
        # 更新当前区间
        cur = num
    else:
        # 如果区间是相交的那么把当前区间的后面元素更新。
        cur[1] = max(cur[1], num[1])
# 最后至少要把当前区间放到结果
res.append(cur)

print(len(res))






