"""
coding: utf8
@time: 2020/12/8 16:25
@author: cjr
@file: 快速排序.py
"""
# 快速排序使用分治的方法，随机选取一个元素当做中间点，把它左面的全部排成比他小的
# 把他右边的全部排成比它大的这样就完成局部排序，然后重复这个过程，完成全部排序。


def partition(begin, end, nums):
    """
    本方法的作用是找到pivot应在的位置
    :param begin:
    :param end:
    :param nums:
    :return:
    """
    pivot = nums[begin]
    # mark是小于pivot的元素的个数
    mark = begin
    for i in range(begin + 1, end + 1):
        # 如果当前元素比pivot小，就说明统计到了一个小于pivot的元素
        # 那么就把当前元素和pivot变换位置，把他放到pivot左面。同时把mark加一。
        if nums[i] < pivot:
            mark += 1
            nums[mark], nums[i] = nums[i], nums[mark]
    # 最后mark就是pivot的位置，我们需要把pivot元素同步的挪到mark位置上。
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark


def quick_sort(begin, end, nums):
    if begin >= end:
        return
    # 首先找到pivot下标
    pivot_index = partition(begin, end, nums)
    # 根据pivot下标进行分治。
    quick_sort(begin, pivot_index - 1, nums)
    quick_sort(pivot_index + 1, end, nums)


if __name__ == '__main__':
    nums_ = [1, 3, 8, 4, 2, 1, 5, 10]
    begin_ = 0
    end_ = len(nums_) - 1
    quick_sort(begin_, end_, nums_)
    print(nums_)


