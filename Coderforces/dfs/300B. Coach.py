import heapq
import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline
MOD = 10 ** 9 + 7


def input_nums():
    return list(map(int, input().split(' ')))


def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]


def merge(a, b):
    x, y = find(a), find(b)
    if x != y:
        p[y] = x

n, m = input_nums()
p = list(range(n + 1))
for _ in range(m):
    a, b = input_nums()
    merge(a, b)

nums = []
d = defaultdict(list)
for i in range(1,n + 1):
    t = find(i)
    d[t].append(i)
    nums.append(t)


print("nums", nums)
cnt = Counter(nums)
print("cnt", cnt)
if any(x > 3 for x in cnt.values()):
    print(-1)
    exit()

l = n // 3
group = [[] for _ in range(l)]
q = sorted(cnt.items(), key=lambda x: x[1], reverse=True)

# for k, v in cnt.items():
for k, v in q:
    print('k, v', k, v)
    flag = False
    for x in group:
        if len(x) + v <= 3:
            x.extend(d[k])
            flag = True
            break
    if not flag:
        # print(k, v, group)
        print(-1)
        exit()

for x in group:
    print(*x)




