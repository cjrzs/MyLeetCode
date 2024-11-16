import heapq
import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

input = sys.stdin.readline


def input_nums():
    return list(map(int, input().split(' ')))


for _ in range(int(input())):
    n = int(input())
    if n == 2:
        print(0)
        continue
    res = []

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if n % 2 == 0:
                if (j - i) % n < n // 2:
                    res.append(1)
                elif (j - i) % n == n // 2:
                    res.append(0)
                else:
                    res.append(-1)
            else:
                if (j - i) % n <= n // 2:
                    res.append(1)
                else:
                    res.append(-1)
    print(*res)

