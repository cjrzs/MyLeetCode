'''
coding:utf8
@Time : 2020/6/20 21:50
@Author : cjr
@File : 132模式.py
题目链接：https://leetcode-cn.com/problems/132-pattern/
'''
import typing


class Solution:
    def find132pattern(self, nums: typing.List[int]) -> bool:
        if len(nums) < 3:
            return False
        mi = [nums[0]]
        for i in range(1, len(nums)):
            mi.append(min(nums[i], mi[-1]))
        print(mi)
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > mi[i]:
                while stack and mi[i] >= stack[-1]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False


if __name__ == '__main__':
    com = Solution()
    print(com.find132pattern([2, 3, 2, 0]))


