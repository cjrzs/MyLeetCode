import sys

from collections import defaultdict


sys.setrecursionlimit(10 ** 9)
n, m = list(map(int, input().split(' ')))
nums = [0] + list(map(int, input().split(' ')))
g = defaultdict(list)
vis = set()
for _ in range(m):
    x, y = list(map(int, input().split(' ')))
    g[x].append(y)
    g[y].append(x)


def minimum_chain(u):
    ans = float("INF")
    q = [u]
    while q:
        a = q.pop()
        ans = nums[a] if ans > nums[a] else ans
        for b in g[a]:
            if b not in vis:
                q.append(b)
                vis.add(b)
    return ans

    # def dfs(u, pre):
    #     if u in vis:
    #         return
    #     vis.add(u)
    #     nonlocal ans
    #     # ans = min(ans, nums[u])
    #     if ans < nums[u]:
    #         ans = nums[u]
    #     for a in g[u]:
    #         if a != pre or pre == -1:
    #             dfs(a, u)
    # dfs(u, -1)


res = 0
for i in range(1, n + 1):
    if i not in vis:
        res += minimum_chain(i)

print(res)

