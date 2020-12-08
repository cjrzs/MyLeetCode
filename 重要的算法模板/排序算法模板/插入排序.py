"""
coding: utf8
@time: 2020/12/8 18:16
@author: cjr
@file: 插入排序.py
"""

# 初始以第一个元素为排序后元素，取所有排序好的元素后第一个位置的元素。
# 在排序好的元素序列中从后往前寻找它应该插入的位置。


def insert_sort(nums):
    n = len(nums)
    for i in range(1, n):
        pre_index = i - 1
        curr = nums[i]
        while pre_index >= 0 and nums[pre_index] > curr:
            # 把pre+1的值后移一位，就相当于8 大于 4， 8的值后移一位到4的位置覆盖4。
            nums[pre_index + 1] = nums[pre_index]
            # pre指针前移
            pre_index -= 1
        # 把当前元素curr插入到pre的下一位，完成插入排序的一次循环
        nums[pre_index + 1] = curr
    return nums


if __name__ == '__main__':
    nums_ = [1, 3, 8, 4, 2, 1, 5, 10]
    insert_sort(nums_)
    print(nums_)

