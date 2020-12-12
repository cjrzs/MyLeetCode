"""
coding: utf8
@time: 2020/12/12 16:43
@author: cjr
@file: LRUCache.py
"""
import collections


class LRUCache:
    """
    缓存淘汰策略：最近最少使用。
    Hash Table + Double LinkedList
    """

    def __init__(self, capacity):
        # 直接使用顺序字典，来保证元素在缓存中的相对顺序
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        # 如果访问到该元素，要把该元素取出来，重新加入字典
        v = self.dic.pop(key)
        self.dic[key] = v
        return v

    def put(self, key, value):
        if key in self.dic:
            self.dic.pop()
        else:
            # 如果还有剩余容量，就把剩余容量-1,就可以直接放进去了
            if self.remain > 0:
                self.remain -= 1
            # 没有剩余容量的话，就要按照先进先出的规则，移除最先进来的元素。
            else:
                # popitem方法可以移除一个键值对，last为False则按照先进先出移除。
                self.dic.popitem(last=False)
        self.dic[key] = value


