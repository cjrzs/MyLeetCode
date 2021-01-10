"""
coding: utf8
@time: 2021/1/10 17:48
@author: cjr
@file: 1014. 登山.py
"""

"""
五一到了，ACM队组织大家去登山观光，队员们发现山上一个有N个景点，并且决定按照顺序来浏览这些景点，即每次所浏览景点的编号都要大于前一个浏览景点的编号。

同时队员们还有另一个登山习惯，就是不连续浏览海拔相同的两个景点，并且一旦开始下山，就不再向上走了。

队员们希望在满足上面条件的同时，尽可能多的浏览景点，你能帮他们找出最多可能浏览的景点数么？

输入格式
第一行包含整数N，表示景点数量。

第二行包含N个整数，表示每个景点的海拔。

输出格式
输出一个整数，表示最多能浏览的景点数。

数据范围
2≤N≤1000
输入样例：
8
186 186 150 200 160 130 197 220
输出样例：
4
"""


def dengshan(nums):
    """
    在<怪盗基德的滑翔翼>基础上，枚举一遍中间点，然后把中间点左面和右面的最大上升子序列加起来
    减去1 （即中间点被统计了两遍） 。
    :param nums:
    :return:
    """
    n = len(nums)
    dp1 = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp1[i] = max(dp1[i], dp1[j] + 1)
    dp2 = [1] * n
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if nums[i] > nums[j]:
                dp2[i] = max(dp2[i], dp2[j] + 1)
    res = 0
    for i in range(n):
        res = max(res, dp1[i] + dp2[i] - 1)
    return res


num = int(input())
buildings = list(map(int, input().split()))
print(dengshan(buildings))

