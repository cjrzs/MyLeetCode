n, d = map(int, str(input()).split(' '))
s = str(input())


def solution():
    res = float("inf")
    mem = {}

    def dfs(u, cnt):
        # print(u, cnt)
        nonlocal res
        if cnt >= res:
            return
        if u in mem:
            if mem[u] > cnt or mem[u] > res:
                return
        mem[u] = cnt
        if u >= n - 1:
            res = cnt
            return
        for x in range(d, 0, -1):
            # print('ux', u, x)
            if u + x < n:
                if s[u + x] == '1':
                    dfs(u + x, cnt + 1)
                else:
                    continue

    dfs(0, 0)
    return res

t = solution()
print(-1 if t == float("inf") else t)




