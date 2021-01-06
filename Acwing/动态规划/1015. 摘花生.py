"""
coding: utf8
@time: 2021/1/6 21:11
@author: cjr
@file: 1015. 摘花生.py
"""

"""
Hello Kitty想摘点花生送给她喜欢的米老鼠。

她来到一片有网格状道路的矩形花生地(如下图)，从西北角进去，东南角出来。

地里每个道路的交叉点上都有种着一株花生苗，上面有若干颗花生，经过一株花生苗就能摘走该它上面所有的花生。

Hello Kitty只能向东或向南走，不能向西或向北走。

问Hello Kitty最多能够摘到多少颗花生。

1.gif

输入格式
第一行是一个整数T，代表一共有多少组数据。

接下来是T组数据。

每组数据的第一行是两个整数，分别代表花生苗的行数R和列数 C。

每组数据的接下来R行数据，从北向南依次描述每行花生苗的情况。每行数据有C个整数，按从西向东的顺序描述了该行每株花生苗上的花生数目M。

输出格式
对每组输入数据，输出一行，内容为Hello Kitty能摘到得最多的花生颗数。

数据范围
1≤T≤100,
1≤R,C≤100,
0≤M≤1000
输入样例：
2
2 2
1 1
3 4
2 3
2 3 4
1 6 5
输出样例：
8
16
"""


from typing import List


class Solution:
    def penats(self, groups: List[List[int]]):
        m, n = len(groups), len(groups[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = groups[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + groups[i][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + groups[0][i]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + groups[i][j]
        # print(f'dp: {dp}')
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    res = []
    groups_num = int(input())
    for i in range(groups_num):
        row_num, col_num = list(map(int, input().split()))
        cur_group = []
        for j in range(row_num):
            cur_group.append(list(map(int, input().split())))
        tmp_res = solution.penats(cur_group)
        res.append(tmp_res)

    for k in res:
        print(k)







