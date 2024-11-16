# import heapq
# import sys
# from collections import defaultdict, Counter, deque
#
# # sys.setrecursionlimit(8 ** 10)
#
# # input = sys.stdin.readline
# sys.stdin=open('input.txt', 'r')
# sys.stdout=open('output.txt', 'w')
# MOD = 10 ** 9 + 7
#
#
# def input_nums():
#     return list(map(int, input().split(' ')))
#
#
# n, m = input_nums()
# q = []
# vis = [[0] * m for _ in range(n)]
# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]
# k = int(input())
# nums = input_nums()
# for i in range(0, len(nums), 2):
#     a, b = nums[i] - 1, nums[i + 1] - 1
#     vis[a][b] = 1
#     q.append((a, b))
#
# while q:
#     # print(q)
#     t = []
#
#     for x, y in q:
#         for i in range(4):
#             a, b = x + dx[i], y + dy[i]
#             if 0 <= a < n and 0 <= b < m and vis[a][b] == 0:
#                 vis[a][b] = 1
#                 t.append((a, b))
#     if not t:
#         print(*[x + 1 for x in q[0]])
#         exit()
#     del q
#     q = t
#
#
#
#

def solve(n, m, k, trees):
    burning_trees = []
    for a in range(0, k * 2, 2):
        burning_trees.append((trees[a], trees[a + 1]))
    last_cost = None
    last_tree = (-1, -1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = min([abs(i - t[0]) + abs(j - t[1]) for t in burning_trees])
            if last_cost is None or cost > last_cost:
                last_cost = cost
                last_tree = (i, j)

    return f"{last_tree[0]} {last_tree[1]}"


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        n, m = map(int, file.readline().split())
        k = int(file.readline())
        trees = list(map(int, file.readline().split()))

    with open("output.txt", "w") as file:
        file.write(solve(n, m, k, trees))

