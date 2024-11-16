n = int(input())
boys = list(map(int, str(input()).split(' ')))
boys.sort()
m = int(input())
girls = list(map(int, str(input()).split(' ')))
girls.sort()

res = 0
i = j = 0
while i < n and j < m:
    x, y = boys[i], girls[j]
    if abs(x - y) <= 1:
        i += 1
        j += 1
        res += 1
    elif x < y:
        i += 1
    elif y < x:
        j += 1
print(res)



