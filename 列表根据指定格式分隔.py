'''
coding:utf8
@Time : 2020/3/4 1:58
@Author : cjr
@File : 列表根据指定格式分隔.py
谨以此纪念第一个严格意义上自己开发的算法！
目的：将列表根据指定格式的字符串分隔成不同几段列表并转换成指定格式
例如：
把列表根据以“-”开头的字符串为界限，分隔成不同的子列表，其中以“-”开头的字符串为字典的key，其后的所有元素为value
转换前：["-x", "1", "2", "3", "-q", "4", "5", "6", "-d", "7", "8"]
转换后：[{'-x': ['1', '2', '3']}, {'-q': ['4', '5', '6']}, {'-d': ['7', '8']}]
'''


class Base:

    def __init__(self, parm_list: list):
        self.parm_list = parm_list

    def count_(self):
        new_list = []
        for item in self.parm_list:
            if item.startswith('-'):
                new_list.append(self.parm_list.index(item))
        return new_list

    def list_to_dict(self, l: list):
        d = {}
        for item in l:
            if item.startswith('-'):
                key = item
            else:
                d.setdefault(key, []).append(item)
        return d

    def parm_to_dict(self) -> list:
        parm_index_list = self.count_()
        # lst = list(filter(lambda x: parm_index_list[x:x+1], self.parm_list))
        result = []
        for i in range(len(parm_index_list)):
            try:
                key_list = self.parm_list[parm_index_list[i]:parm_index_list[i+1]]
                new_list = self.list_to_dict(key_list)
                result.append(new_list)
            except IndexError:
                key_list = self.parm_list[parm_index_list[i]:]
                new_list = self.list_to_dict(key_list)
                result.append(new_list)
        return result