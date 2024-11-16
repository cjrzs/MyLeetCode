import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline


def input_nums():
    return list(map(int, input().split(' ')))

g = {}

n, p = input_nums()
duin = [0] * (n + 1)
duout = [0] * (n + 1)
for _ in range(p):
    a, b, w = input_nums()
    g[a] = (b, w)
    duin[b] += 1
    duout[a] += 1
# print(duin, duout)
water_box = set()
water_exit = set()
for i in range(1, n + 1):
    if duin[i] and not duout[i]:
        water_exit.add(i)
    if not duin[i] and duout[i]:
        water_box.add(i)

# print(water_box, water_exit)

res = []
for start in water_box:
    node, val = g[start]
    t = [start, node, val]
    while node not in water_exit:
        node, val = g[node]
        t[1] = node
        t[2] = min(t[2], val)
    res.append(t)
print(len(res))
for item in res:
    print(*item)








