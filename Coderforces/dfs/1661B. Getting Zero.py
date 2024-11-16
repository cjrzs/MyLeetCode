n = int(input())
nums = list(map(int, input().split(' ')))

mod = 32768

vis = [[-1 for _ in range(16)] for _ in range(mod + 1)]

def dfs(u, cnt):
    if u % 32768 == 0:
        return cnt
    if cnt > 15:
        return 32768
    if vis[u % mod][cnt] != -1:
        return vis[u % mod][cnt]
    vis[u % mod][cnt] = min(dfs(u + 1, cnt + 1), dfs(u * 2, cnt + 1))
    return vis[u % mod][cnt]


dist = [dfs(num, 0) for num in range(32769)]
for x in nums:
    print(dist[x], end=" ")





