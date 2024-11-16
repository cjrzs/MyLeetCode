from collections import defaultdict


def dfs(x: str, level: int):
    if (x, level) in vis:
        return
    vis.add((x, level))
    if x not in g:
        global res
        res = max(res, level)
        return
    for i in g[x]:
        dfs(i, level + 1)


g = defaultdict(list)
n = int(input())
nums = []
res = 0
for _ in range(n):
    x, _, y = input().split(' ')
    x: str = x.lower()
    y: str = y.lower()
    g[x].append(y)
    nums.append(x)
# print(g, nums)
vis = set()
for x in nums:
    dfs(x, 1)
print(res)



