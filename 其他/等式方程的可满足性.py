'''
coding:utf8
@Time : 2020/6/8 17:01
@Author : cjr
@File : 等式方程的可满足性.py
题目链接：https://leetcode-cn.com/problems/satisfiability-of-equality-equations/
'''
from typing import List


class Solution:
    class UnionFind:
        def __init__(self):
            self.parent = list(range(26))

        def find(self, index):
            if index == self.parent[index]:
                return index
            self.parent[index] == self.find(self.parent[index])
            return self.parent[index]

        def union(self, index1, index2):
            self.parent[self.find(index1)] = self.find(index2)

    @staticmethod
    def equationsPossible(equations: List[str]) -> bool:
        """
        官方题解
        :param equations:
        :return:
        """
        uf = Solution.UnionFind()
        for st in equations:
            if st[1] == '=':
                index1 = ord(st[0]) - ord('a')
                print(index1)
                index2 = ord(st[3]) - ord('a')
                print(index2)
                uf.union(index1, index2)
        for st in equations:
            if st[1] == '!':
                index1 = ord(st[0]) - ord('a')
                print(index1)
                index2 = ord(st[3]) - ord('a')

                if uf.find(index1) == uf.find(index2):
                    return False
        return True

    @staticmethod
    def equationsPossible2(equations: List[str]) -> bool:
        d = {a: a for a in 'abcdefghijklmnopqrstuvwxyz'}
        nset = set()

        def root(x):
            print(x, '-----', d[x])
            if x != d[x]:
                d[x] = root(d[x])
            return d[x]

        for a, m, n, b in equations:
            # 元素中如果存在“！=”则放入nset
            if m == '!':
                nset.add((a, b))    # nset = {('u', 'h')}
                print(nset)
            # 元素中存在“==”则将b的值给a。
            else:
                d[root(a)] = root(b)     # 执行完这步d中的q变成h
        for i, j in nset:
            '''
             eq中该元素的下标0,3在nset中，说明存在该元素存在“！=”的情况。
             此时判断该元素的下标0,3对应字符是否相同，如果相同说明存在该元素为“==”的情况。
             此时两种情况都存在，如果0,3对应字符相同，则结果必为False。
             因为题目中说“只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false”。 
            '''

            if root(i) == root(j):
                return False
        return True

    @staticmethod
    def equationsPossible3(equations: List[str]) -> bool:
        pass


if __name__ == '__main__':
    res = Solution.equationsPossible2(["q==h", "u!=h"])
    print(res)

