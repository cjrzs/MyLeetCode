import heapq
import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline
MOD = 10 ** 9 + 7


def input_nums():
    return list(map(int, input().split(' ')))


n = int(input())
nums = [0] + list(map(int, input().split(' ')))
g = defaultdict(list)
res = 0
tree = []
for _ in range(int(input())):
    a, b, w = map(int, input().split(' '))
    if nums[a] > nums[b]:
        tree.append((a, b, w))
tree.sort(key=lambda x: x[2])
num = 1
vis = [0] * (n + 1)
# print(tree)
for a, b, w in tree:
    if vis[b] == 0:
        vis[b] = 1
        res += w
        num += 1
    if num == n:
        break
if num == n:
    print(res)
    exit()
else:
    print(-1)








