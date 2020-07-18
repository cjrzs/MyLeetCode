'''
coding:utf8
@Time : 2020/7/18 19:57
@Author : cjr
@File : 连续子数组的最大和.py
题目链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        状态转移方程：
        当 dp[i−1]>0 时：执行 dp[i]=dp[i−1]+nums[i] ；
        当 dp[i−1]≤0 时：执行 dp[i]=nums[i] ；
        时间复杂度：O(n)
        空间复杂度：O(1)

        :param nums:
        :return:
        """
        n = len(nums)

        for i in range(1, n):
            nums[i] = max(nums[i - 1], 0) + nums[i]
            # print(f'num[{i}]: {nums[i]}')
        return max(nums)

    def maxSubArray2(self, nums: List[int]) -> int:
        """
        dp模板写法，题解同上
        :param nums:
        :return:
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            if dp[i - 1] > 0:
                dp[i] = max(dp[i - 1], dp[i - 1] + nums[i])
            else:
                dp[i] = nums[i]
        return max(dp)


if __name__ == '__main__':
    com = Solution()
    res = com.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(res)



