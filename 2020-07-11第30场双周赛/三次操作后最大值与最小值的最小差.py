'''
coding:utf8
@Time : 2020/7/11 23:44
@Author : cjr
@File : 三次操作后最大值与最小值的最小差.py
给你一个数组 nums ，每次操作你可以选择 nums 中的任意一个数字并将它改成任意值。

请你返回三次操作后， nums 中最大值与最小值的差的最小值。



示例 1：
输入：nums = [5,3,2,4]
输出：0
解释：将数组 [5,3,2,4] 变成 [2,2,2,2].
最大值与最小值的差为 2-2 = 0 。

示例 2：
输入：nums = [1,5,0,10,14]
输出：1
解释：将数组 [1,5,0,10,14] 变成 [1,1,0,1,1] 。
最大值与最小值的差为 1-0 = 1 。

示例 3：
输入：nums = [6,6,0,1,1,4,6]
输出：2

示例 4：
输入：nums = [1,5,6,14,15]
输出：1

提示：

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
'''
from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        n1 = list(sorted(nums))
        return min(n1[-1] - n1[3], n1[-2] - n1[2], n1[-3] - n1[1], n1[-4] - n1[0])



