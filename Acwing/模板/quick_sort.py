"""
coding: utf8
@time: 2021/1/16 11:49
@author: cjr
@file: quick_sort.py


1、分解成子问题
左小右大的话，如果当前i值比分割值大就停止移动i，如果当前j值比分割值小就停止移动j。
然后交换i， j对应的值。
2、递归处理子问题
以j为分界线分成两段。
3、合并递归的结果。（在快排中不需要这一步骤）
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

