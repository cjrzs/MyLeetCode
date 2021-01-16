"""
coding: utf8
@time: 2021/1/16 11:49
@author: cjr
@file: quick_sort.py
"""


def quick_sort(nums, l, r):
    if l >= r:
        return
    x, i, j = nums[l], l - 1, r + 1
    while l < r:
        while True:
            i += 1
            if nums[i] >= x:
                break
        while True:
            j -= 1
            if nums[j] <= x:
                break
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            break
    quick_sort(nums, l, j)
    quick_sort(nums, j + 1, r)


n = int(input())
nums = list(map(int, input().split()))
quick_sort(nums, 0, n - 1)
print(' '.join(nums))

