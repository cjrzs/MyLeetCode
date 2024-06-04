'''
coding:utf8
@Time : 2020/6/3 22:23
@Author : cjr
@File : 新21点.py
题目链接：https://leetcode-cn.com/problems/new-21-game/
'''


class Solution:
    """
    在题解抄的答案
    时间复杂度=格子长度O(K+W)，空间复杂度=格子长度O(K+W)
    """
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [None] * (K+W)
        # 总分数tmp
        tmp = 0
        # 当结束时候为分数不能抽排分数大于K，则无法抽卡了
        # 此时概率只有可以确定的两种情况0和1。（边界条件）
        for i in range(K, K+W):
            if i <= N:
                dp[i] = 1
            else:
                dp[i] = 0
            tmp += dp[i]
        for i in range(K-1, -1, -1):
            dp[i] = tmp/W
            tmp = tmp - dp[i+W] + dp[i]
        return dp[0]


if __name__ == '__main__':
    com = Solution()
    print(com.new21Game(10, 1, 10))


