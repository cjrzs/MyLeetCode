from functools import lru_cache


@lru_cache()
def solution(n, m):
    if n == m:
        return True
    elif n % 3 != 0:
        return False
    else:
        return solution(n // 3, m) or solution(2 * n // 3, m)


T = int(input())
for _ in range(T):
    n, m = list(map(int, str(input()).split(' ')))
    if solution(n, m):
        print("YES")
    else:
        print("NO")



