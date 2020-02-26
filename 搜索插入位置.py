'''
coding:utf8
@Time : 2020/2/26 23:47
@Author : cjr
@File : 搜索插入位置.py
'''


class Solution:
    """
    基础思路：当数组中的值大于或者等于目标值时候直接返回该值位置，并且break
    设置边界，当数组中最后一个值也小于目标值的时候，直接返回数组长度。
    """
    def searchInsert(self, nums: list, target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
                break
            elif nums[-1] < target:
                return len(nums)

    """
    标准的二分查找思路，设定首尾边界取中值与目标值进行比较
    """
    def searchInsert2(self, nums: list, target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end)/2
            mid = int(mid)
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                return mid
        return start





