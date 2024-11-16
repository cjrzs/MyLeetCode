T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, str(input()).split(' ')))
    res = []
    idx = -1
    for i in range(1, n):
        if nums[i] != nums[0]:
            idx = i
            res.append((1, i + 1))
    if idx == -1:
        print("NO")
        continue
    for i in range(1, n):
        if nums[i] == nums[0]:
            res.append((idx + 1, i + 1))
    print("YES")
    for x, y in res:
        print(f"{x} {y}")










