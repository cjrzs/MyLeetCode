def computer_game(nums):
    # print(nums)
    n = len(nums[0])
    vis = set()
    def dfs(x, y):
        # print(x, y)
        if x == 1 and y == n - 1:
            return True
        vis.add((x, y))
        for i, j in ((1, 0), (1, 1), (0, 1), (-1, 1)):
            a, b = x + i, y + j
            if 0 <= a < 2 and 0 <= b < n and nums[a][b] == '0' and (a, b) not in vis:
                if dfs(a, b):
                    return True
        return False
    return dfs(0, 0)

T = int(input())
for _ in range(T):
    n = int(input())
    g = []
    g.append(list(input()))
    g.append(list(input()))
    print("YES" if computer_game(g) else "NO")







