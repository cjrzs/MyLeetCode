"""
coding: utf8
@time: 2020/12/3 22:18
@author: cjr
@file: 计数质数.py
题目链接：https://leetcode-cn.com/problems/count-primes/
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        """
        埃氏筛
        :param n:
        :return:
        """
        # counts判断个数
        counts = 0
        # 初始化n大小的数组表示是不是质数，如果是则为1，不是则是0。
        is_primes = [1] * n
        for i in range(2, n):
            # 判断是否是质数，是的话 质数个数就加一个
            if is_primes[i]:
                counts += 1
                # 这里因为质数的倍数一定不是质数，因为质数本身就是质数倍数的因子
                # 又因为如果从2i 开始标记是冗余的 因为这些数在i 之前就被其他倍数标记过了
                # 所以我们直接从i * i 开始标记
                for j in range(i * i, n, i):
                    is_primes[j] = 0
        return counts

    def countPrimes1(self, n: int) -> int:
        """
        线性筛
        :param n:
        :return:
        """
        # 存放质数
        primes = []
        is_primes = [1] * n
        for i in range(2, n):
            # 如果是质数放到质数数组里
            if is_primes[i] == 1:
                primes.append(i)
            j = 0
            while primes[j] * i < n:
                # 标记质数集合中和 i 相乘的数，因为他们有了质数这个因子所以不是0，道理同埃氏筛。
                is_primes[primes[j] * i] = 0

                if i % primes[j] == 0:
                    break
                j += 1
        return len(primes)


