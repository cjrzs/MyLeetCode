T = int(input())
for _ in range(T):
    n, m = list(map(int, str(input()).split(' ')))
    a = list(map(int, str(input()).split(' ')))
    p = set((map(int, str(input()).split(' '))))
    while True:
        ok = False
        for i in range(n - 1):
            if i + 1 in p and a[i] > a[i + 1]:
                ok = True
                a[i], a[i + 1] = a[i + 1], a[i]
        if not ok:
            break
    ok = True
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            ok = False
    print("YES" if ok else "NO")









