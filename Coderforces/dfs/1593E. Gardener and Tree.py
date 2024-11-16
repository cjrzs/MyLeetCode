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


def input_nums():
    return list(map(int, input().split(' ')))


for _ in range(int(input())):
    input()
    n, k = input_nums()
    g: List[List[int]] = [[] for _ in range(n + 1)]
    indo: List[int] = [0] * (n + 1)
    for _ in range(n - 1):
        a, b = input_nums()
        g[a].append(b)
        g[b].append(a)
        indo[a] += 1
        indo[b] += 1
    if n == 1:
        print("0")
        continue
    # print(indo)
    q = deque()
    res = 0
    vis = [False] * (n + 1)
    for i in range(1, n + 1):
        if indo[i] == 1:
            q.append(i)
            res += 1
            indo[i] -= 1
    # print(indo)
    k -= 1
    while k and q:
        # print(q)
        t = deque()
        cnt = len(q)
        for idx in range(cnt):
            u = q.popleft()
            for x in g[u]:
                indo[x] -= 1
                if indo[x] == 1:
                    t.append(x)
                    res += 1
        # print(t)
        # print(indo)
        q = t
        k -= 1
    print(n - res)






