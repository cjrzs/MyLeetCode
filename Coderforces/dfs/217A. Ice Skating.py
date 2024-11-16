from collections import defaultdict

n = int(input())
nums = [[-1, -1]]
res = 0
p = [0] * 105
for i in range(1, n + 1):
    p[i] = i


def find(i):
    if i != p[i]:
        p[i] = find(p[i])
    return p[i]


for i in range(1, n + 1):
    # print(dx, dy)
    x, y = list(map(int, str(input()).split(' ')))
    nums.append((x, y))
    for j in range(1, i):
        q = nums[j]
        if q[0] == x or q[1] == y:
            a = find(i)
            b = find(j)
            p[a] = b
# print(p)

for i in range(1, n + 1):
    if i == p[i]:
        res += 1
print(res - 1)





