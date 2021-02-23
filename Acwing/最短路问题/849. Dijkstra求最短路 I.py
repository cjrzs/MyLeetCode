"""
coding: utf8
@time: 2021/2/23 22:33
@author: cjr
@file: 849. Dijkstra求最短路 I.py
给定一个n个点m条边的有向图，图中可能存在重边和自环，所有边权均为正值。

请你求出1号点到n号点的最短距离，如果无法从1号点走到n号点，则输出-1。

输入格式
第一行包含整数n和m。

接下来m行每行包含三个整数x，y，z，表示存在一条从点x到点y的有向边，边长为z。

输出格式
输出一个整数，表示1号点到n号点的最短距离。

如果路径不存在，则输出-1。

数据范围
1≤n≤500,
1≤m≤105,
图中涉及边长均不超过10000。

输入样例：
3 3
1 2 2
2 3 1
1 3 4
输出样例：
3
"""
n, m = map(int, input().split())
# 建图，数据范围来看是稠密图，边的数量远大于点数量的平方，所以用邻接矩阵，复杂度是n^2
g = [[float('inf')] * (n + 1) for _ in range(n + 1)]
# 初始化邻接矩阵
for _ in range(m):
    x, y, w = map(int, input().split())
    # 因为题目中说有重边，所以要取最短的
    g[x][y] = min(g[x][y], w)
# d就是该算法中第一个点到其他所有点的最短路径。全部初始化为正无穷。
d = [float('inf')] * (n + 1)
# 第一个点到他自己的最短路径初始化为0
d[1] = 0
# st表示每个点是否有被确定
st = set()
for _ in range(n):
    t = -1
    for i in range(1, n + 1):
        # 如果i不是已经确定的点并且
        # i是等于初值的点或者最短路径中i比t更短则更新t
        if i not in st and (i == -1 or d[t] > d[i]):
            t = i
        # 已经确定的点添加到st
        st.add(t)
    # 用t更新其他点的距离
    for i in range(1, n + 1):
        d[i] = min(d[i], d[t] + g[t][i])
print(-1 if d[-1] == float('inf') else d[-1])














