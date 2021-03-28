"""
coding: utf8
@time: 2021/3/28 17:15
@author: cjr
@file: 还原排列的最少操作步数.py

给你一个偶数n，已知存在一个长度为 n 的排列 perm ，其中perm[i] == i​（下标 从 0 开始 计数）。

一步操作中，你将创建一个新数组arr，对于每个i：

如果 i % 2 == 0 ，那么 arr[i] = perm[i / 2]
如果 i % 2 == 1 ，那么 arr[i] = perm[n / 2 + (i - 1) / 2]
然后将 arr​​ 赋值​​给 perm 。

要想使 perm 回到排列初始值，至少需要执行多少步操作？返回最小的 非零 操作步数。

示例 1：
输入：n = 2
输出：1
解释：最初，perm = [0,1]
第 1 步操作后，perm = [0,1]
所以，仅需执行 1 步操作

示例 2：
输入：n = 4
输出：2
解释：最初，perm = [0,1,2,3]
第 1 步操作后，perm = [0,2,1,3]
第 2 步操作后，perm = [0,1,2,3]
所以，仅需执行 2 步操作

示例 3：
输入：n = 6
输出：4
 

提示：
2 <= n <= 1000
n是一个偶数
"""


def change(nums):
    a = []
    n = len(nums)
    for i in range(n):
        if i % 2 == 1:
            a.append(nums[int(n / 2 + (i - 1) / 2)])
        else:
            a.append(nums[int(i / 2)])
    return a


class Solution:
    """
    直接模拟即可。
    """
    def reinitializePermutation(self, n: int) -> int:
        s = []
        cnt = 1
        for i in range(n):
            s.append(i)
        a = change(s)
        while a != s:
            a = change(a)
            cnt += 1
        return cnt






