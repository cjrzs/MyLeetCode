'''
coding:utf8
@Time : 2020/6/13 23:52
@Author : cjr
@File : 二分查找.py
题目链接：https://leetcode-cn.com/problems/binary-search/
'''
import typing


class Solution:
    def search(self, nums: typing.List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0
        while left <= right:
            print(f'right:{right}')
            print(f'left:{left}')
            mid = (right - left) // 2
            mid = mid + left
            print(f'mid:{mid}')
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # 区间是[left, mid-1]
                right = mid - 1
            else:
                # 搜索区间是[mid+1, right]
                left = mid + 1
        return -1


if __name__ == '__main__':
    com = Solution()
    # print(com.search([-1,0,3,5,9,12], 9))
    print(com.search([2, 5], 5))
