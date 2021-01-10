"""
coding: utf8
@time: 2021/1/10 20:43
@author: cjr
@file: 1016. 最大上升子序列和.py
"""
'''
一个数的序列 bi，当 b1<b2<…<bS 的时候，我们称这个序列是上升的。

对于给定的一个序列(a1,a2,…,aN)，我们可以得到一些上升的子序列(ai1,ai2,…,aiK)，这里1≤i1<i2<…<iK≤N。

比如，对于序列(1,7,3,5,9,4,8)，有它的一些上升子序列，如(1,7),(3,4,8)等等。

这些子序列中和最大为18，为子序列(1,3,5,9)的和。

你的任务，就是对于给定的序列，求出最大上升子序列和。

注意，最长的上升子序列的和不一定是最大的，比如序列(100,1,2,3)的最大上升子序列和为100，而最长上升子序列为(1,2,3)。

输入格式
输入的第一行是序列的长度N。

第二行给出序列中的N个整数，这些整数的取值范围都在0到10000(可能重复)。

输出格式
输出一个整数，表示最大上升子序列和。

数据范围
1≤N≤1000
输入样例：
7
1 7 3 5 9 4 8
输出样例：
18
'''


def Solution(nums):
    n = len(nums)
    dp = [nums[i] for i in range(n)]
    dp[0] = nums[0]
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + nums[i])
    return max(dp)


num = int(input())
nums = list(map(int, input().split()))
# print(nums)
print(Solution(nums))



















