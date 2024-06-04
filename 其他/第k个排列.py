"""
coding:utf8
@Time : 2020/9/5 11:38
@Author : cjr
@File : 第k个排列.py
题目链接：https://leetcode-cn.com/problems/permutation-sequence/
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        直接全排列，然后取第k个，不过这种暴力方法会tql
        :param n:
        :param k:
        :return:
        """
        res = []
        track = []
        nums = []
        for i in range(1, n + 1):
            nums.append(str(i))

        def dfs(nums, track):
            if len(nums) == len(track):
                return res.append(track[:])
            for i in range(len(nums)):
                if nums[i] in track:
                    continue
                track.append(nums[i])
                dfs(nums, track)
                track.pop()
                
        dfs(nums, track)
        result = ''.join(res[k - 1])
        return result


if __name__ == '__main__':
    x = Solution()
    print(x.getPermutation(3, 3))
