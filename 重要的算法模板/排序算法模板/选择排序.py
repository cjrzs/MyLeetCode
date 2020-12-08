"""
coding: utf8
@time: 2020/12/8 17:28
@author: cjr
@file: 选择排序.py
"""
# 每次都在所有的元素中选出最小的排在前面已经排序好的元素后面


def selection_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


if __name__ == '__main__':
    nums_ = [1, 3, 8, 4, 2, 1, 5, 10]
    print(selection_sort(nums_))





