"""
coding: utf8
@time: 2021/1/16 14:21
@author: cjr
@file: merge_sort.py
"""


def merge_sort(nums, l, r):
    if l >= r:
        return
    mid = (l + r) >> 1
    merge_sort(nums, l, mid)
    merge_sort(nums, mid + 1, r)

    tmp, i, j = [], l, mid + 1

    while i <= mid and j <= r:
        if nums[i] < nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1
    while i <= mid:
        tmp.append(nums[i])
        i += 1
    while j <= r:
        tmp.append(nums[j])
        j += 1
    for idx, i in enumerate(tmp):
        nums[l + idx] = i


n = int(input())
nums = list(map(int, input().split()))

merge_sort(nums, 0, n - 1)
print(nums)

