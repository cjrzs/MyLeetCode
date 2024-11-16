def func(nums):
    n = len(nums)
    t = ['00', '25', '50', '75']

    def helper(suffix):
        res = 0
        i = n - 1
        while i >= 0 and nums[i] != suffix[-1]:
            res += 1
            i -= 1
        if i > 0:
            u = i - 1
        else:
            return float("inf")
        while u >= 0 and nums[u] != suffix[0]:
            res += 1
            u -= 1
        return res

    res = float("inf")
    for item in t:
        res = min(res, helper(item))
    return res

T = int(input())
for _ in range(T):
    nums = input()
    print(func(nums))
