from functools import lru_cache

n = int(input())
nums = list(map(int, str(input()).split(' ')))

res = []

@lru_cache()
def dfs(i):
    vis = set()
    u = i
    while u < n + 1:
        if u in vis:
            return u
        vis.add(u)
        u = nums[u - 1]


for i in range(1, n + 1):
    res.append(dfs(i))

print(' '.join([str(x) for x in res]))

