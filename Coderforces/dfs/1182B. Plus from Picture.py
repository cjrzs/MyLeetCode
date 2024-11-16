import sys
from collections import defaultdict, Counter

sys.setrecursionlimit(8 ** 10)
input = sys.stdin.readline

n, m = list(map(int, input().split(' ')))
nums = []
cnt = 0
for _ in range(n):
    t: str = input()
    cnt += t.count('*')
    nums.append(t)


def func():
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if nums[i][j] == nums[i - 1][j] == nums[i + 1][j] == nums[i][j - 1] == nums[i][j + 1] == '*':
                a, b = i, j
                res = 0
                while a - 1 >= 0 and nums[a - 1][b] == '*':
                    a -= 1
                    res += 1
                a, b = i, j
                while a + 1 < n and nums[a + 1][b] == '*':
                    a += 1
                    res += 1
                a, b = i, j
                while b - 1 >= 0 and nums[a][b - 1] == '*':
                    b -= 1
                    res += 1
                a, b = i, j
                while b + 1 < m and nums[a][b + 1] == '*':
                    b += 1
                    res += 1
                return res
    return -1


res = func()
# print(f"{res + 1, cnt}")
if res == -1:
    print("NO")
else:
    print("YES" if res + 1 == cnt else "NO")







