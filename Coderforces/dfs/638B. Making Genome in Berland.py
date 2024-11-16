import heapq
import sys
import threading
from collections import defaultdict, Counter, deque

from typing import List, Set, Dict, Tuple

input = sys.stdin.readline
MOD = 10 ** 9 + 7


def input_nums():
    return list(map(int, input().split(' ')))

def main() -> None:
    n = int(input())
    total: Set[int] = set(range(n + 1))
    nums: List[str] = [""]
    for _ in range(n):
        nums.append(input().strip())

    g: Dict[int, List[Tuple[int, int]]] = defaultdict(list)

    def check(i: int, j: int) -> int:
        # print(i, j)
        t = 0
        for x in range(min(len(nums[i]), len(nums[j]))):
            # print(nums[i][len(nums[i]) - x - 1:], nums[j][:x + 1])
            if nums[i][len(nums[i]) - x - 1:] == nums[j][:x + 1]:
                t = x + 1
        return t

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                t = check(i, j)
                if t:
                    g[i].append((j, t))

    # print(g)

    def func(start: int) -> Tuple[float, str]:
        vis: List[bool] = [False] * (n + 1)
        vis[start] = True
        res_length = float("inf")
        res = ""
        path = set()

        def dfs(u: int, pre: int, cnt: int, s: str):
            nonlocal res_length, res
            # if not g[u] or level == n + 1:
            # l = cnt + sum(len(nums[x]) for x in total - set(path) if nums[x] not in s)
            if cnt >= res_length:
                return
            else:
                res_length = cnt
                # res = s + "".join(nums[x] for x in total - set(path) if nums[x] not in s)
                res = s

            for x, w in g[u]:
                if not vis[x] and x != pre:
                    vis[x] = True
                    dfs(x, u, cnt + len(nums[x]) - w, s + nums[x][w: ])
                    vis[x] = False

        dfs(start, -1, len(nums[start]), nums[start])
        for i in range(1, n + 1):
            if i not in path:
                dfs(start, -1, len(nums[start]), nums[start])
        # print(res_length, res)
        return res_length, res


    q = float("inf")
    res = ""
    for i in range(1, n + 1):
        l, s = func(i)
        if l < q:
            q = l
            res = s
    print(res)


sys.setrecursionlimit(10 ** 6)
threading.stack_size(1 << 27)
thread = threading.Thread(target=main)
thread.start()
thread.join()




