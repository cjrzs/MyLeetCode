import heapq
import sys
import threading
from collections import defaultdict, Counter, deque
from itertools import permutations, chain, combinations
from types import GeneratorType

from typing import List, Set, Dict, Tuple, AnyStr

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


def topsort(indu: List[int], g: defaultdict) -> List:
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


def is_bipartite_graph(g: defaultdict, n: int) -> bool:
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


def input_nums():
    return list(map(int, input().split(' ')))


n, m = input_nums()
nums = [-1] + input_nums()
g = [set() for _ in range(max(nums) + 1)]
max_vertex = [-1, -1]
vis = set()
for _ in range(m):
    a, b = input_nums()
    x, y = nums[a], nums[b]
    if x != y:
        g[x].add(y)
        g[y].add(x)


res = min(nums[1:])
for i in range(1, max(nums) + 1):
    if len(g[i]) > len(g[res]):
        res = i
print(res)

# q = deque()
# q.append((1, -1))
# while q:
#     t = deque()
#     u, pre = q.popleft()
# for u in range(1, n + 1):
#     cnt = set()
#     # if not g[u]:
#     cnt.add(nums[u])
#     # if vis[u] == 0:
#     #     vis[u] = 1
#     for x in g[u]:
#         print(u, x)
#         # if nums[x] != nums[u]:
#         cnt.add(nums[x])
#         # if x != pre:
#         #     q.append((x, u))
#     if len(cnt) > max_vertex[0] or (len(cnt) == max_vertex[0] and nums[u] < nums[max_vertex[1]]):
#         max_vertex[0] = len(cnt)
#         max_vertex[1] = u
#     print(u, max_vertex)
#
# print(nums[max_vertex[1]])

