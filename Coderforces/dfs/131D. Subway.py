import heapq
import sys
import threading
from collections import defaultdict, Counter, deque
from itertools import permutations, chain, combinations
from types import GeneratorType

from typing import List, Set, Dict, Tuple

input = sys.stdin.readline
MOD = 10 ** 9 + 7


def bootstrap(f, stack=[]):
    def wrapped_func(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrapped_func


def topsort(indu: List[int], g: List[List[int]]) -> List:
    """
    把图g按照拓扑序列进行排序。
    :param indu: 图的入度
    :param g: 使用 defaultdict 进行建图。
    :return:
    """
    res = []
    q = deque()
    for i in range(26):
        if indu[i] == 0:
            q.append(i)
    # print(q, g)
    # print(indu)
    while q:
        u = q.popleft()
        res.append(chr(u + 97))
        for x in g[u]:
            indu[x] -= 1
            if not indu[x]:
                q.append(x)
    return res


def is_bipartite_graph(g: List[List[int]], n: int) -> bool:
    """
    染色法判断一个图是不是二分图
    :param g: 图，使用 defaultdict 进行建图。
    :param n: 图中点的数量
    :return:
    """
    color = [0] * (n + 1)
    for i in range(1, n + 1):
        if color[i] != 0:
            continue
        color[i] = 1
        q = deque()
        q.append(i)
        while q:
            u = q.popleft()
            for x in g[u]:
                if not color[x]:
                    color[x] = 3 - color[u]
                    q.append(x)
                else:
                    if color[x] == color[u]:
                        return False
    return True


def find_loop_in_pseudo_tree(g: List[List[int]]) -> List[int]:
    """
    基环树找环：基环树是比普通的树多了一条边，从而在树中形成一个环，
    本函数会找到所有在环上的节点。
    :param g: 存储树
    :return: mark[i]的取值为0或者1，其中1表示i是环中的节点。
    """
    flag = 0
    vis = [0] * (n + 1)
    mark = [0] * (n + 1)

    @bootstrap
    def dfs(u, pre):
        nonlocal flag
        if vis[u]:  # 找到环
            if not flag:
                flag = u
                mark[u] = mark[pre] = 1
            yield
        vis[u] = 1
        for v in g[u]:
            if v == pre:
                continue
            yield dfs(v, u)
            # 在递归返回时处理环上的点
            if v != flag and mark[v]:
                mark[u] = 1
        yield

    dfs(1, -1)
    return mark


def input_nums():
    return list(map(int, input().split(' ')))


n = int(input())
g = [[] for _ in range(n + 1)]
for _ in range(n):
    a, b = input_nums()
    g[a].append(b)
    g[b].append(a)
#
# flag = 0
# vis = [0] * (n + 1)
# mark = [0] * (n + 1)
# dist = [0] * (n + 1)
# loop = []


# @bootstrap
# def dfs(u, pre):
#     global flag
#     if vis[u]:  # 找到环
#         if not flag:
#             flag = u
#             mark[u] = mark[pre] = 1
#             loop.append(u)
#             loop.append(pre)
#         yield
#     vis[u] = 1
#     for v in g[u]:
#         if v == pre:
#             continue
#         yield dfs(v, u)
#         # 在递归返回时处理环上的点
#         if v != flag and mark[v]:
#             if not mark[u]:
#                 loop.append(u)
#             mark[u] = 1
#     yield

dist = [0] * (n + 1)
@bootstrap
def cal_dist(u, pre):
    for x in g[u]:
        if x != pre and not mark[x]:
            dist[x] = dist[u] + 1
            yield cal_dist(x, u)
    yield


mark = find_loop_in_pseudo_tree(g)
# print(mark)
for i in range(1, n + 1):
    if mark[i]:
        cal_dist(i, -1)

print(*dist[1: ])







