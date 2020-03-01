'''
coding:utf8
@Time : 2020/3/2 0:19
@Author : cjr
@File : 最大子序和.py
题目链接：https://leetcode-cn.com/problems/maximum-subarray/
'''


class Solution:
    """
    题解思路：
    1、定义变量tmp来存储当前的子串和，定义变量max_存储最大和
    2、从第二个元素遍历数组。
    3、如果当前子串和加上此时元素的值（i）大于当前子串和，那么最大值记录更新成前子串和+当前值
    同时当前存储的子串和（tmp）也要更新成前子串和+当前值。
    4、如果前子串和加上此时元素的值（i）小于当前子串和，那么最大值记录更新，
    同时更新当前存储的子串和为当前值，这样下次寻找会以当前值为起点继续寻找。
    """
    def maxSubArray(self, nums: list) -> int:
        tmp = nums[0]
        max_ = tmp
        for i in range(1, len(nums)):
            if nums[i]+tmp > tmp:
                max_ = max(max_, nums[i]+tmp)
                tmp = nums[i]+tmp
            else:
                max_ = max(tmp, nums[i], tmp+nums[i], max_)
                tmp = nums[i]
        return max_


