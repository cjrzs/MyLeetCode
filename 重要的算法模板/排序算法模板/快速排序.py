"""
coding: utf8
@time: 2020/12/8 16:25
@author: cjr
@file: 快速排序.py
"""
# 快速排序使用分治的方法，随机选取一个元素当做中间点，把它左面的全部排成比他小的
# 把他右边的全部排成比它大的这样就完成局部排序，然后重复这个过程，完成全部排序。


def partition(begin, end, nums):
    pivot = nums[begin]
    mark = begin
    for i in range(begin + 1, end + 1):
        if nums[i] < pivot:
            mark += 1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark


def quick_sort(begin, end, nums):
    if begin >= end:
        return
    pivot_index = partition(begin, end, nums)
    quick_sort(begin, pivot_index - 1, nums)
    quick_sort(pivot_index + 1, end, nums)


if __name__ == '__main__':
    nums_ = [1, 3, 8, 4, 2, 1, 5, 10]
    begin_ = 0
    end_ = len(nums_) - 1
    quick_sort(begin_, end_, nums_)
    print(nums_)


