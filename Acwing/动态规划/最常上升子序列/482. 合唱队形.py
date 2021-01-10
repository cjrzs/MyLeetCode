"""
coding: utf8
@time: 2021/1/10 18:22
@author: cjr
@file: 482. 合唱队形.py
"""
"""
N位同学站成一排，音乐老师要请其中的(N-K)位同学出列，使得剩下的K位同学排成合唱队形。     

合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1，2…，K，他们的身高分别为T1，T2，…，TK，  
则他们的身高满足T1<…<Ti>Ti+1>…>TK(1≤i≤K)。     

你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。

输入格式
输入的第一行是一个整数N，表示同学的总数。

第二行有n个整数，用空格分隔，第i个整数Ti是第i位同学的身高(厘米)。

输出格式
输出包括一行，这一行只包含一个整数，就是最少需要几位同学出列。

数据范围
2≤N≤100,
130≤Ti≤230
输入样例：
8
186 186 150 200 160 130 197 220
输出样例：
4
"""


def hechangduixing(nums):
    n = len(nums)
    dp1 = dp2 = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp1[i] = max(dp1[i], dp1[j] + 1)
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if nums[i] > nums[j]:
                dp2 = max(dp2[i], dp2[j] + 1)
    res = 0
    for i in range(n):
        res = max(res, dp1[i] + dp2[i] - 1)
    return n - res


N = int(input())
nums = [map(int, input().split())]
print(hechangduixing(nums))


