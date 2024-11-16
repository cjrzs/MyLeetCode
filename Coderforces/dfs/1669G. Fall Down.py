def func(nums, n, m):
    j = 0
    while j < m:
        last = n
        for i in range(n - 1, -1, -1):
            if nums[i][j] == 'o':
                last = i
            if nums[i][j] == '*':
                nums[i][j], nums[last - 1][j] = nums[last - 1][j], nums[i][j]
                last -= 1
        j += 1


T = int(input())
for _ in range(T):
    nums = []
    n, m = list(map(int, str(input()).split(' ')))
    for i in range(n):
        nums.append(list(str(input())))
    func(nums, n, m)
    for row in nums:
        print(''.join(row))
    # print('-------')


