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


def main():
    s = input().strip()
    g: List[List[int]] = [[] for _ in range(26)]
    indo = [0] * 26
    d = [[False] * 26 for _ in range(26)]
    for i in range(1, len(s)):
        a, b = ord(s[i - 1]) - 97, ord(s[i]) - 97

        if not d[a][b] and not d[b][a]:
            d[a][b] = True
            d[b][a] = True
            g[a].append(b)
            g[b].append(a)
            indo[a] += 1
            indo[b] += 1
    # print(g)
    # print(indo)
    if any(x > 2 for x in indo):
        print("NO")
        return
    res = []
    vis: List[bool] = [False] * 26
    q = deque()
    for i in range(26):
        if not indo[i]:
            vis[i] = True
            res.append(chr(i + 97))
        elif indo[i] == 1:
            q.append(i)
            vis[i] = True
    while q:
        # print(q)
        u = q.pop()
        res.append(chr(u + 97))
        for x in g[u]:
            if not vis[x]:
                q.append(x)
                vis[x] = True
    if len(res) < 26:
        print("NO")
        return
    print("YES")
    print("".join(res))

for _ in range(int(input())):
    main()




