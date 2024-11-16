import heapq
import sys
import threading
from collections import defaultdict, Counter, deque
from itertools import permutations, chain, combinations
from types import GeneratorType

from typing import List, Set, Dict, Tuple

input = sys.stdin.readline
MOD = 10 ** 9 + 7


def bootstrap(f, stack=[]):
    def wrapped_func(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrapped_func


def input_nums():
    return list(map(int, input().split(' ')))


n = int(input())
nums = []
for _ in range(n):
    nums.append(input().strip())

# print(nums)
g = defaultdict(list)
now = nums[0]
indu = [0] * 26
for x in nums[1: ]:
    q, p = len(now), len(x)
    if now.startswith(x):
        print("Impossible")
        exit()
    l = min(q, p)
    i = 0
    while i < l:
        if now[i] != x[i]:
            g[ord(now[i]) - 97].append(ord(x[i]) - 97)
            indu[ord(x[i]) - 97] += 1
            break
        i += 1
    now = x


res = []
q = deque()
for i in range(26):
    if indu[i] == 0:
        q.append(i)
# print(q, g)
# print(indu)
while q:
    u = q.popleft()
    res.append(chr(u + 97))
    for x in g[u]:
        indu[x] -= 1
        if not indu[x]:
            q.append(x)

# print(res)
if len(res) < 26:
    print("Impossible")
else:
    print("".join(res))


