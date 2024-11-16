import sys
from collections import defaultdict, Counter

sys.setrecursionlimit(8 ** 10)


n = int(input())
nums = list(map(int, input().split(' ')))
p = list(range(n + 1))
rank = [0] * (n + 1)


def find(x):
    # print(x, p[x])
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

for i, x in enumerate(nums):
    t = i + 1
    a = find(x)
    b = find(t)
    if a != b:
        # if rank[a] > rank[b]:
        #     p[b] = a
        # elif rank[a] < rank[b]:
        #     p[a] = b
        # else:
        #     p[a] = b
        #     rank[a] += 1
        p[a] = b

# print(p)
unique_roots = set(find(i) for i in range(1, n + 1))
print(len(unique_roots))
# res = set(i for i in p)
# print(len(res) - 1)
