from collections import defaultdict

T = int(input())

for _ in range(T):
    g = defaultdict(list)
    n, m = map(int, input().split(' '))
    for _ in range(m):
        x, y = map(int, input().split(' '))
        g[x].append(y)
        g[y].append(x)
    # print(g)

    three_set = set()
    two_set = set()
    one_node = 0

    for node in range(1, n + 1):
        if len(g[node]) == 1:
            three_set.add(node)

    for node in range(1, n + 1):
        if node not in three_set:
            # print('not in three_set', node, g[node])
            if all(x not in three_set for x in g[node]):
                one_node = node
    # print(three_set, one_node, '======')
    x_num = len(g[one_node])
    y_num = len(three_set) // x_num
    print(x_num, y_num)




