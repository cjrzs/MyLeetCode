"""
coding: utf8
@time: 2021/1/6 22:14
@author: cjr
@file: 1018. 最低通行费.py
"""


"""
一个商人穿过一个N×N的正方形的网格，去参加一个非常重要的商务活动。

他要从网格的左上角进，右下角出。

每穿越中间1个小方格，都要花费1个单位时间。

商人必须在(2N-1)个单位时间穿越出去。

而在经过中间的每个小方格时，都需要缴纳一定的费用。

这个商人期望在规定时间内用最少费用穿越出去。

请问至少需要多少费用？

注意：不能对角穿越各个小方格（即，只能向上下左右四个方向移动且不能离开网格）。

输入格式
第一行是一个整数，表示正方形的宽度N。

后面N行，每行N个不大于100的整数，为网格上每个小方格的费用。

输出格式
输出一个整数，表示至少需要的费用。

数据范围
1≤N≤100
输入样例：
5
1  4  6  8  10 
2  5  7  15 17 
6  8  9  18 20 
10 11 12 19 21 
20 23 25 29 33
输出样例：
109
样例解释
样例中，最小值为109=1+2+5+7+9+12+19+21+33。
"""


from typing import List


class Solution:
    def business(self, group: List[List[int]]):
        m, n = len(group), len(group[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        # 这个地方为什么这么初始化？
        dp[0][1], dp[1][0] = 0, 0
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + group[i - 1][j - 1]
        return dp[-1][-1]

    def business2(self, group: List[List[int]]):
        m, n = len(group), len(group[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = group[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + group[i][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + group[0][i]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + group[i][j]
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    row = int(input())
    group = []
    for i in range(row):
        group.append(list(map(int, input().split())))
    res = solution.business(group)
    print(res)





