import sys
from collections import defaultdict, Counter

sys.setrecursionlimit(8 ** 10)

# input = sys.stdin.readline


def input_nums():
    return list(map(int, input().split(' ')))

path = []
def dfs(x, cnt):
    # if (x, cnt) in vis:
    #     return
    # vis.add((x, cnt))
    # print(x, cnt)
    if cnt == n - 1:
        if x == 'a':
            # print(path[:])
            global res
            res += 1
        return
    for c in ('a', 'b', 'c', 'd', 'e', 'f'):
        t = x + c

        if t in d:
            # path.append(c)
            # print(t)
            dfs(d[t], cnt + 1)
            # path.pop()


n, q = input_nums()
d = {}
res = 0
vis = set()
for _ in range(q):
    x, y = input().split(' ')
    d[x] = y
# print(d)

for u in ('a', 'b', 'c', 'd', 'e', 'f'):
    dfs(u, 0)
print(res)





