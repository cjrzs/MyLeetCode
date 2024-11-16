n = int(input())
d = []

for i in range(n):
    t = int(input())
    d.append(t)

def solution():
    # def dfs(u, level):
    #     mem.add(u)
    #     if u < 0:
    #         return level
    #     else:
    #         return dfs(d[u] - 1, level + 1)

    res = 0
    for i in range(n):
        c = 0
        while i >= 0:
            i = d[i] - 1
            c += 1
        res = max(res, c)
    return res
print(solution())

