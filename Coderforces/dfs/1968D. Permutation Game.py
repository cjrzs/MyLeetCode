import sys
from collections import defaultdict

sys.setrecursionlimit(8 ** 10)


def func(start, k):
    d = []
    vis = set()
    t = start
    val = 0
    while t not in vis and k:
        vis.add(t)
        d.append(val + a[t - 1] * k)
        val += a[t - 1]
        k -= 1
        t = p[t - 1]
    return d


T = int(input())
for _ in range(T):
    n, k, pb, ps = list(map(int, input().split(' ')))
    p = list(map(int, input().split(' ')))
    a = list(map(int, input().split(' ')))

    posdb = func(pb, k)
    posds = func(ps, k)
    # print("posdb, posds", posdb, posds)
    mb = max(posdb)
    ms = max(posds)
    if mb > ms:
        print("Bodya")
    elif mb < ms:
        print("Sasha")
    else:
        print("Draw")



