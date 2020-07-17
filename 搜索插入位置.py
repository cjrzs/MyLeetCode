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
    题目链接：https://leetcode-cn.com/problems/search-insert-position/
    2020/07/17的每日一题
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
        # 当首尾节点相同时，还需判断一次该节点。
        while start <= end:
            # 取中值，当数组长度为奇数时，取向左取整
            mid = (start + end)//2
            # 当目标小于当前中值时候，右节点变成mid-1 是因为中值此时已经和目标值比较过了
            if target < nums[mid]:
                end = mid - 1
            # 当目标大于当前中值时候同理，需要把左节点变成mid+1 因为此时中值已经比较过了。
            elif target > nums[mid]:
                start = mid + 1
            else:
                return mid
        return start





