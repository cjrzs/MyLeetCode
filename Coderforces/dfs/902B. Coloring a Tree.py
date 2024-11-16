import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 8)

n = int(input())
g = defaultdict(list)

for i, x in enumerate(input().split(' ')):
    g[int(x)].append(i + 2)

c = input().split(' ')
# print(g)
res = 1


def dfs(u, cur_color):
    if c[u - 1] != cur_color:
        global res
        res += 1
        cur_color = c[u - 1]
    if u not in g:
        return
    for i in g[u]:
        dfs(i, cur_color)

dfs(1, c[0])
print(res)







