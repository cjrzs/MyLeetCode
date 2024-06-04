'''
coding:utf8
@Time : 2020/6/24 23:59
@Author : cjr
@File : 最接近的三数之和.py
题目链接：
'''
import typing


class Solution:
    def threeSumClosest(self, nums: typing.List[int], target: int) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return sum(nums)
        nums.sort()
        res = float('inf')

        for i in range(len(nums)):
            # 当两个数相等时候 直接进入下一次循环
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            t = target - nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:

                # 当三个数和target相等时候直接返回targe即可
                if t - nums[left] - nums[right] == 0:
                    return target
                s = nums[i] + nums[left] + nums[right]
                if s < target:
                    left += 1
                else:
                    right -= 1
                if abs(s - target) < abs(res - target):
                    res = s
        return res


if __name__ == '__main__':
    com = Solution()
    print(com.threeSumClosest([-1,2,1,-4], 2))










