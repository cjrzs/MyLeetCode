'''
coding:utf8
@Time : 2020/6/7 21:06
@Author : cjr
@File : 1比特与2比特字符.py
题目链接：https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/
'''
from typing import List


class Solution:
    """
    官方题解：
    我们可以对 bits 数组从左到右扫描来判断最后一位是否为一比特字符。当扫描到第 i 位时，
    如果 bits[i]=1，那么说明这是一个两比特字符，将 i 的值增加 2。如果 bits[i]=0，
    那么说明这是一个一比特字符，将 i 的值增加 1。

    如果 i 最终落在了bits.length−1 的位置，那么说明最后一位一定是一比特字符。
    """
    """
    设定i为0，从前往后数，遇到1跳两位，遇到0跳一位
    只要有1的存在，就会与下一位组成2比特，不管下一位是1还是0。
    只要是0就是1比特。
    因为最后一位必定是0，所以只要判断len(bits)前一位就可以了。
    如果i最后落在len(bits)-1，那么说明前面全部判断结束，就剩最后一位0
    所以一定是1比特，如果没有落在len(bits)-1，说明是2比特
    """
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        # i是从0开始的，所以边界条件要-1
        while i < n - 1:
            if bits[i] == 0:
                i += 1
            elif bits[i] == 1:
                i += 2
        return i == n - 1

