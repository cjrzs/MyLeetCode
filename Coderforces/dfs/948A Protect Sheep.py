n, m = map(int, str(input()).split())

nums = []
for _ in range(n):
    nums.append(list(str(input())))

def func(nums):
    for i in range(n):
        for j in range(m):
            # if nums[i][j] == 'S':
            for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                a, b = i + x, j + y
                if 0 <= a < n and 0 <= b < m:
                    if nums[a][b] == '.':
                        nums[a][b] = 'D'
                    if nums[i][j] == 'S' and nums[a][b] == 'W':
                        return "No"
    return "Yes"

t = func(nums)
if t == 'No':
    print(t)
if t == 'Yes':
    print(t)
    for item in nums:
        print(''.join(item))








