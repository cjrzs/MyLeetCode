'''
coding:utf8
@Time : 2020/7/11 15:51
@Author : cjr
@File : 计算右侧小于当前元素的个数.py
题目链接：https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/
'''
from typing import List


class Solution:
    """
    这个真的不会以后再更新
    2020 07 11
    """
    def countSmaller(self, nums: List[int]) -> List[int]:
        dict1 = {}
        res = []
        for i in range(len(nums)):
            dict1[i] = nums[i]
        tmp = sorted(dict1.items(), key=lambda kv: kv[1])
        print(tmp)
        for i in range(len(tmp)):
            if i < len(tmp) - 1 and tmp[i][1] == tmp[i + 1][1]:
                continue
            else:
                res.insert(tmp[i][0] - 1, 0)
        return res


if __name__ == '__main__':
    com = Solution()
    print(com.countSmaller([5, 2, 6, 1]))
