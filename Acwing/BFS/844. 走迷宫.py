"""
coding: utf8
@time: 2021/2/20 18:25
@author: cjr
@file: 844. 走迷宫.py
给定一个n*m的二维整数数组，用来表示一个迷宫，数组中只包含0或1，其中0表示可以走的路，1表示不可通过的墙壁。

最初，有一个人位于左上角(1, 1)处，已知该人每次可以向上、下、左、右任意一个方向移动一个位置。

请问，该人从左上角移动至右下角(n, m)处，至少需要移动多少次。

数据保证(1, 1)处和(n, m)处的数字为0，且一定至少存在一条通路。

输入格式
第一行包含两个整数n和m。

接下来n行，每行包含m个整数（0或1），表示完整的二维数组迷宫。

输出格式
输出一个整数，表示从左上角移动至右下角的最少移动次数。

数据范围
1≤n,m≤100
输入样例：
5 5
0 1 0 0 0
0 1 0 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0
输出样例：
8
"""
from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
mark = [[-1] * m for _ in range(n)]


def bfs():
    # 初始化队列，初始节点和向量表示向四面走。
    queue = deque([])
    queue.append([0, 0])
    idx, idy = [1, -1, 0, 0], [0, 0, 1, -1]
    mark[0][0] = 0

    while queue:
        cur = queue.popleft()
        # 向四个方向走动
        for i in range(4):
            x = cur[0] + idx[i]
            y = cur[1] + idy[i]
            # x，y在合法范围并且不是墙壁并且没有走过（也就是不能回头，因为求最短路径）
            if 0 <= x < n and 0 <= y < m and not maze[x][y] and mark[x][y] == -1:
                queue.append([x, y])
                # print(cur[0], cur[1])
                mark[x][y] = mark[cur[0]][cur[1]] + 1
    # print(mark)
    return mark[-1][-1]


print(bfs())




