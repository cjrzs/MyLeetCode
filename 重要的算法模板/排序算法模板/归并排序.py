"""
coding: utf8
@time: 2020/12/9 12:32
@author: cjr
@file: 归并排序.py
"""

# 归并排序与快速排序差不多，归并是先把整个数组分成两份子序列，
# 先然后不断的调用归并排序函数，使得两个子序列都有序，
# 最后合并成一个大排序好的序列。


def merge(nums, left, mid, right):
    res = []
    # i是第一个有序数组的开头，j是第二个有序数组的开头
    i = left
    j = mid + 1
    # 先全部比较，从两个排序数组中选出来首位较小的放在结果集中
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            res.append(nums[i])
            i += 1
        else:
            res.append(nums[j])
            j += 1
    # 当完成上面操作之后，还会有i或者j未全部完成，在将剩余未完成的放入结果集。
    while i <= mid:
        res.append(nums[i])
        i += 1
    while j <= right:
        res.append(nums[j])
        j += 1
    # 因为要在原数组的基础上排序，所以把结果集给原数组。
    nums[left: right + 1] = res


def merge_sort(nums, left, right):
    if left >= right:
        return
    mid = (left + right) >> 1
    merge_sort(nums, left, mid)
    merge_sort(nums, mid + 1, right)
    merge(nums, left, mid, right)


if __name__ == '__main__':
    nums_ = [1, 3, 8, 4, 2, 1, 5, 10]
    begin_ = 0
    end_ = len(nums_) - 1
    merge_sort(nums_, begin_, end_, )
    print(nums_)
