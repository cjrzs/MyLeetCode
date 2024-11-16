n, t = list(map(int, str(input()).split(' ')))
nums = list(map(int, str(input()).split(' ')))
flag = False
i = 1
while i <= t:
    if i == t:
        flag = True
        print("YES")
        break
    else:
        if i <= n:
            i = i + nums[i - 1]
        else:
            flag = True
            print("NO")
            break

if not flag:
    print("NO")


