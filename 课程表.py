"""
coding:utf8
@Time : 2020/8/4 11:23 
@Author : CJR  
@File : 课程表.py
题目链接：https://leetcode-cn.com/problems/course-schedule/
"""
from typing import List
from collections import deque


class Solution:
    """
    入度表。BFS
    参考题解：
    https://leetcode-cn.com/problems/course-schedule/solution/course-schedule-tuo-bu-pai-xu-bfsdfsliang-chong-fa/
    https://leetcode-cn.com/problems/course-schedule/solution/ke-cheng-biao-by-leetcode-solution/
    下面这个题解有关于
    https://leetcode-cn.com/problems/course-schedule/solution/ke-cheng-biao-san-jian-ke-zhi-ke-cheng-biao-iladyb/
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 图中所有节点入度
        indegrees = [0 for _ in range(numCourses)]
        print(f'初始化indegrees： {indegrees}')
        # 邻接表。
        adjacency = [[] for _ in range(numCourses)]
        print(f'初始化adjacency： {adjacency}')
        queue = deque()
        # 根据题目要求，进一步初始化入度表与邻接表
        # 前面元素表示想学习的课程，我们放在入度表
        # 后面元素是先决条件，我们放在邻接表
        for cur, pre in prerequisites:
            print(f'cur: {cur}    pre: {pre}')
            indegrees[cur] += 1
            print(f'indegrees: {indegrees}')
            adjacency[pre].append(cur)
            print(f'adjacency: {adjacency}')
        # 把入度表中为0的元素入队
        # 为什么这样做？
        # 因为如果图没有环，那么最后所有元素都该是0
        # 我们现在把已经是0的入队，来找他们的临接节点
        # 把该节点出队的同时， 临接节点的入度 -1
        # 就是indegrees[cur] -= 1
        # 这样做之后代表cur的入度为0，代表其没有了前驱节点
        # 循环后，最后结果如果为空代表没有环，则所有课程都能学（True）
        for i in range(len(indegrees)):
            if not indegrees[i]:
                queue.append(i)
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in indegrees[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)
        return not numCourses


if __name__ == '__main__':
    x = Solution()
    x.canFinish(2, [[1,0]])

