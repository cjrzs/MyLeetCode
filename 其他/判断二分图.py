'''
coding:utf8
@Time : 2020/7/16 23:20
@Author : cjr
@File : 判断二分图.py
题目链接：https://leetcode-cn.com/problems/is-graph-bipartite/
'''
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        # 三种颜色类型， 未染色， 红色， 绿色
        UN, RED, GREEN = 0, 1, 2
        # 颜色初始化
        color = [UN] * n
        # 是否是二分图
        valid = True

        # dfs深度优先遍历
        def dfs(node: int, c: int):
            nonlocal valid
            # 染色
            color[node] = c
            # 判断邻节点颜色
            c_nei = (GREEN if c == RED else RED)
            for neighbor in graph[node]:
                if color[neighbor] == UN:
                    dfs(neighbor, c_nei)
                    if not valid:
                        return
                elif color[neighbor] != c_nei:
                    valid = False
                    return
        for i in range(n):
            print(f'color[{i}]: {color[i]}')
            if color[i] == UN:
                dfs(i, RED)
                if not valid:
                    break
        return valid


if __name__ == '__main__':
    com = Solution()
    print(com.isBipartite([[1,3], [0,2], [1,3], [0,2]]))


