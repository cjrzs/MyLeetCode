n, m = list(map(int, str(input()).split(' ')))
nums = []
for _ in range(n):
    nums.append(list(str(input())))


def fulfill(x, y):
    if (x + y) & 1:
        nums[x][y] = 'B'
    else:
        nums[x][y] = 'W'


for i in range(n):
    for j in range(m):
        if nums[i][j] == '.':
            fulfill(i, j)

for i in nums:
    print(''.join(i))

