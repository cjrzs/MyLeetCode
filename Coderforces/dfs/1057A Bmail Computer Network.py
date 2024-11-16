if __name__ == '__main__':
    n = int(input())
    nums = [0] + list(map(int, str(input()).split(' ')))
    # print(n, nums)
    res = [n]
    t = n
    while t - 1 >= 0:
        res.append(nums[t - 1])
        t = nums[t - 1]
        # print(nums[t - 1])

    ans = ' '.join([str(x) for x in res[::-1][1: ]])
    print(ans)



