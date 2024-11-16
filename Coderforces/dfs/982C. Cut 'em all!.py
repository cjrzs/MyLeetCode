# import heapq
# import sys
# import threading
# from collections import defaultdict, Counter, deque
#
# # sys.setrecursionlimit(8 ** 10)
#
# input = sys.stdin.readline
# MOD = 10 ** 9 + 7
#
#
# def input_nums():
#     return list(map(int, input().split(' ')))
#
# n = int(input())
# if n % 2 == 1:
#     print(-1)
#     exit()
# g = defaultdict(list)
# size = [1] * (n + 1)
# for _ in range(n - 1):
#     a, b = input_nums()
#     a -= 1
#     b -= 1
#     g[a].append(b)
#     g[b].append(a)
#
# x = [-1] * n
# c = [1] * n
# q = [0]
# while q:
#     a = q[-1]
#     f = 1
#     for i in g[a]:
#         if x[i] == -1:
#             x[i] = a
#             q.append(i)
#             if f == 1:
#                 f = 0
#     if f:
#         b = q.pop()
#         c[x[b]] += c[b]
#
# # print(size)
# print(sum(1 for i in c if i % 2 == 0))


from collections import defaultdict
import threading
from sys import stdin, setrecursionlimit

setrecursionlimit(300000)
input = stdin.readline


def dfs(node, g, par, sz):
    for i in g[node]:
        if i != par:
            sz[node] += dfs(i, g, node, sz)
    return sz[node] + 1


def main():
    n = int(input())
    if n % 2 != 0:
        print(-1)
        exit(0)
    g = defaultdict(list)
    for i in range(n - 1):
        x, y = map(int, input().strip().split())
        g[x - 1].append(y - 1)
        g[y - 1].append(x - 1)

    sz = [0] * (n)
    tt = []
    dfs(0, g, -1, sz)
    res = 0
    # print(sz)
    for i in range(1, n):
        if sz[i] % 2 != 0:
            res += 1
    print(res)


threading.stack_size(10 ** 8)
t = threading.Thread(target=main)
t.start()
t.join()

