'''
coding:utf8
@Time : 2020/5/6 22:33
@Author : cjr
@File : 盛水最多的容器.py
题目链接：https://leetcode-cn.com/problems/container-with-most-water/
'''


class Solution:
    def maxArea(self, height: list) -> int:
        """
        暴力法：
        双重循环 直接求出所有可能的容量，取最大值，但是如果数组太大运行时间太长
        :param height:
        :return:
        """
        ls_x = len(height)
        res = 0
        for x in range(0, ls_x):
            for m in range(x+1, ls_x):
                tmp = min(height[m], height[x]) * (m-x)
                res = max(tmp, res)
        return res

    def maxArea2(self, height: list) -> int:
        res = 0
        start = 0
        end = len(height) - 1
        while end > start:
            if height[end] >= height[start]:
                res = max(res, (end - start) * min(height[end], height[start]))
                start += 1
            else:
                res = max(res, (end - start) * min(height[end], height[start]))
                end -= 1
        return res

if __name__ == '__main__':
    com = Solution()
    print(com.maxArea2([1,8,6,2,5,4,8,3,7]))




