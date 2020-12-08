"""
coding: utf8
@time: 2020/12/8 17:18
@author: cjr
@file: 冒泡排序.py
"""

# 冒泡排序使用当前元素与下一个元素做比较，把符合条件的后移一位或者不动，
# 这样每次都会把最大或者最小的数放在最后一个位置。
# 重复这种排序思路。就可以从后到前的排序好数组。


def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


if __name__ == '__main__':
    nums_ = [1, 3, 8, 4, 2, 1, 5, 10]
    print(bubble_sort(nums_))















