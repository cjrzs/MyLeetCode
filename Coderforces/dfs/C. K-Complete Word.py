import sys
from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(8 ** 10)

# input = sys.stdin.readline


def input_nums():
    return list(map(int, input().split(' ')))


T = int(input())
for _ in range(T):
    n, k = input_nums()
    s = input()
    res = 0
    for i in range(k):
        d = [0] * 26
        for j in range(i, n, k):
            d[ord(s[j]) - 97] += 1
            print(k-1-j, s[k-1-j])
            d[ord(s[k - 1 - j]) - 97] += 1
        # print(d)
        res += sum(d) - max(d)
    print(res // 2)
    # print('------------')


