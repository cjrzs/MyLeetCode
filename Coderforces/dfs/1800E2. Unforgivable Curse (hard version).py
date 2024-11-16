import heapq
import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline


def input_nums():
    return list(map(int, input().split(' ')))


# def bfs(u):
#     v = end[u]
#     q = [(u, -1)]
#     d = set()
#     d.add(u)
#     while q:
#         cur, pre = q.pop()
#         if start[cur] == v:
#             return True
#         for x in g[cur]:
#             if x != pre and x not in d:
#                 d.add(x)
#                 if start[x] == v:
#                     vis[x] = 1
#                     vis[u] = 1
#                     return True
#                 q.append((x, cur))
#     # print(u, start[u], end[u])
#     return False


for _ in range(int(input())):
    n, k = input_nums()
    start = list(input().strip())
    end = list(input().strip())
    if sorted(start) != sorted(end):
        print("NO")
    else:
        if k < n:
            t = n - k
            if start[t: -t] != end[t: -t]:
                print("NO")
            else:
                print("YES")
        else:
            if start != end:
                print("NO")
            else:
                print("YES")

    # g = defaultdict(list)
    # vis = [0] * n
    # for i, x in enumerate(list(start)):
    #     if i + k < n:
    #         g[i].append(i + k)
    #         g[i + k].append(i)
    #     if i + k + 1 < n:
    #         g[i].append(i + k + 1)
    #         g[i + k + 1].append(i)
    # flag = True
    # for i in range(n):
    #     if start[i] != end[i]:
    #         if not bfs(i) and vis[i] == 0:
    #             flag = False
    #             break
    # print("YES" if flag else "NO")


