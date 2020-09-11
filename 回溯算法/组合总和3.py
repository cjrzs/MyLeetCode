"""
coding:utf8
@Time : 2020/9/11 23:12
@Author : cjr
@File : 组合总和3.py
题目链接：https://leetcode-cn.com/problems/combination-sum-iii/
"""
from typing import List


class Solution:
    """
    经过了一段时间对回溯的学习，已经能独立完成中等难度的回溯题目
    """
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        本题就是一道经典的对于回溯的应用
        是组合总和的第三道题
        :param k:
        :param n:
        :return:
        """
        # 定义res接收最后的结果
        res = []

        # dfs遍历
        def dfs(sums, k, start, track):
            # 经典回溯模板，这里定义结束条件
            # 本题的结束条件就是k和n的限制
            if len(track) == k and sums == 0:
                res.append(track[:])
                return
            # 因为路径最多只有1~9的正整数，所以直接定义[start, 10]， start初始值为1
            for i in range(start, 10):
                # sums初始值是n。进入回溯模板，sums-i就是代表第一次遍历后剩下的值
                sums -= i
                # i推入track
                track.append(i)
                # 因为不允许有重复数字，所以再遍历start的值就是i + 1
                dfs(sums, k, i + 1, track)
                # 下面两句是根据模板进行回溯
                sums += i
                track.pop()
        # 使用初始化的值，进行遍历
        dfs(n, k, 1, [])
        # 返回结果
        return res



