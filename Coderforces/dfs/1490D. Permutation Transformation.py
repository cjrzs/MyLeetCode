def func(nums):
    res = [0] * len(nums)
    # print("nums", nums)
    def dfs(l, r, deep):
        # print("l, r", l, r, deep)
        if l > r:
            return
        if l == r:
            res[l] = deep
            return
        t = max(nums[l: r + 1])
        idx = d[t]
        # print("idx", idx)
        res[idx] = deep
        # print(res[:])
        dfs(l, idx - 1, deep + 1)
        dfs(idx + 1, r, deep + 1)
    dfs(0, n - 1, 0)
    return res


T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, str(input()).split(' ')))
    d = {}
    for i, x in enumerate(nums):
        d[x] = i
    # print(d)
    res = func(nums)

    print(' '.join([str(x) for x in res]))
    # print('----------')






