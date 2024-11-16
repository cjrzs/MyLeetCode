from functools import lru_cache

a, b = list(map(int, str(input()).split(' ')))


@lru_cache()
def dfs(a, b, path):
    path += ' ' + str(a)
    if  a == b:
        return path
    elif a > b:
        return
    return dfs(a * 2, b, path) or dfs(a * 10 + 1, b, path)

res = dfs(a, b, "")
if res:
    print("YES")
    print(len(res.split(' ')) - 1)
    print(res[1: ])
else:
    print("NO")



