"""
coding: utf8
@time: 2020/11/23 16:45
@author: cjr
@file: 跳跃游戏2.py
题目链接：https://leetcode-cn.com/problems/jump-game-ii/
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        count, end, maxx = 0, 0, 0
        for i in range(len(nums) - 1):  # 这里因为最后一个点不用跳跃，所以最大长度要减一
            maxx = max(maxx, nums[i] + i)  # 实时更新每个点所能跳到的最远的点。
            # 如果i等于end，说明已经到达了本次循环所能到达的最远距离，那么跳到最远的点
            # 例如：【2， 3， 1， 1， 4】 从头开始循环，第一次可以跳到值 3或者1。
            # 此时end和i都是0， 所以end == i，end更新成maxx也就是2。 此时end  == 2
            # 第一次获取可到达的最远点为下标2，也就是第一个值为1的点。
            # 在这中间的过程中，当i == 1时候maxx最大。最大为nums[1] + i == 4
            # 所以在接下来的循环中如果i == 2时候就可以和end相等了，此时更新end为maxx 也就是4。
            # 这样我们就保证了每次都跳到最大值，也就是一次 end == i 就可以跳跃一次，增加一次跳跃次数。
            if end == i:
                end = maxx
                count += 1
        return count




