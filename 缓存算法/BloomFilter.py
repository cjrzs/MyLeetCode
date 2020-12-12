"""
coding: utf8
@time: 2020/12/12 19:40
@author: cjr
@file: BloomFilter.py
"""

# bit_array存储二进制
from bitarray import bitarray
import mmh3


class BloomFilter:

    def __init__(self, size, hash_num):
        # size是存储数组的大小
        self.size = size
        # hash_num指一个元素进来分成几个二进制位
        self.hash_num = hash_num
        # 初始化二进制数组并且全部设置成0
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, s):
        for seed in range(self.hash_num):
            # 每次都把seed和s做一个hash，并且取模，防止越界
            result = mmh3.hash(s, seed) % self.size
            # 将对应二进制数组中的位置设置成1
            self.bit_array[result] = 1
            print(self.bit_array)

    def lookup(self, s):
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % self.size
            if self.bit_array[result] == 0:
                return 'Nope'
        return 'Probably'


if __name__ == '__main__':

    bf = BloomFilter(500, 7)
    bf.add('cjr')
    print(bf.lookup('cjr'))
    print(bf.lookup('cjr1`23'))



