T = int(input())

for _ in range(T):
    ids = [0]
    nums = str(input())
    n = len(nums)
    for i, x in enumerate(nums):
        if x == 'R':
            ids.append(i + 1)
    ids.append(n + 1)
    res = 0
    for i in range(1, len(ids)):
        res = max(res, ids[i] - ids[i - 1])
    print(res)







