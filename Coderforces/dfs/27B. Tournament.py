import sys
from collections import defaultdict, Counter

sys.setrecursionlimit(8 ** 10)
input = sys.stdin.readline

n = int(input())
du1 = [0] * (n + 1)
du2 = [0] * (n + 1)

for _ in range(n * (n - 1) // 2 - 1):
    t = input()
    x, y = list(map(int, t.split(' ')))
    du1[x] += 1
    du2[y] += 1


res = []
for x in range(1, n + 1):
    if du1[x] + du2[x] != n - 1:
        res.append(x)

res.sort(key=lambda x: -du1[x])
# print(res)
# print(du1, du2)

# if du1[res[0]] > du2[res[1]]:
#     print(res[0], end=" ")
#     print(res[1], end=" ")
#     print()
# else:
#     print(res[1], end=" ")
#     print(res[0], end=" ")
#     print()
print(*res)
