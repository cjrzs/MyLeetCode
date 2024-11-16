import sys
from collections import defaultdict

sys.setrecursionlimit(8 ** 10)


def dfs(l, r):
    # print(l, r)
    if r - l == 1:
        if nums[l] > nums[r]:
            if nums[l] - nums[r] > 1:
                return False
            else:
                # print("0000", l, r)
                global res
                res += 1
        else:
            if nums[r] - nums[l] > 1:
                return False
        return True
    mid = (l + r) // 2
    lmi = min(nums[l: mid + 1])
    lmx = max(nums[l: mid + 1])
    rmx = max(nums[mid + 1: r + 1])
    rmi = min(nums[mid + 1: r + 1])
    # print(f"l: {l}, r: {r}, mid: {mid}")
    if rmi > lmi:
        if rmx - lmi > (r - l):
            return False
    else:
        if lmx - rmi > (r - l):
            return False
        # print("0000", l, r)
        res += 1
    return dfs(l, mid) and dfs(mid + 1, r)


T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split(' ')))
    res = 0
    # print("---------")
    if n == 1 and nums[0] == 1:
        print(0)
        continue
    n -= 1
    if dfs(0, n):
        print(res)
    else:
        print(-1)


