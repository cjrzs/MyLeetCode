T = int(input())
for _ in range(T):
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(list(map(int, str(input()).split(' '))))
    nums = list(enumerate(nums))
    nums.sort(key=lambda x: (x[1][0], -x[1][1]))
    # print(nums)
    ans = [0] * n
    for u, x in enumerate(nums):
        i: int = x[0]
        v: list = x[1] # v = [l, r]
        if u == n - 1 or v[0] == v[1]:
            v.append(v[0])
        elif v[0] == nums[u + 1][1][0]:  # 两个左面相等
            v.append(nums[u + 1][1][1] + 1)
        elif v[1] == nums[u + 1][1][1]:
            v.append(nums[u + 1][1][0] - 1)
        ans[i] = v
    for item in ans:
        print(' '.join([str(x) for x in item]))
    print(' ')





