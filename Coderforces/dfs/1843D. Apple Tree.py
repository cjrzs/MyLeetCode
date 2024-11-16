import threading
from collections import defaultdict

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def main():
    # 自底向上的递归。
    def dfs(x, root):
        if len(g[x]) == 1 and x != 1:
            cnt[x] = 1
            return cnt[x]
        for i in g[x]:
            if i != root:
                t = dfs(i, x)
                # print('t', t, i, x)
                cnt[x] += t
        return cnt[x]

    T = int(input())
    for _ in range(T):
        n = int(input())
        g = defaultdict(list)
        for _ in range(n - 1):
            x, y = list(map(int, str(input()).split(' ')))
            g[x].append(y)
            g[y].append(x)
        # print(g)
        cnt = [0] * (n + 1)
        dfs(1, 1)
        # print(cnt)
        q = int(input())
        for _ in range(q):
            a, b = list(map(int, str(input()).split(' ')))
            print(cnt[a] * cnt[b])
threading.stack_size(2*10 ** 8)
t = threading.Thread(target=main)
t.start()
t.join()




