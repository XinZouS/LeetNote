'''
Medium  https://www.lintcode.com/problem/590/
给一个图中的 n 个节点, 记为 1 到 n .在开始的时候图中没有边.
你需要完成下面两个方法：
        1. connect(a, b), 添加一条连接节点 a, b的边
        2. query(a), 返回图中含 a 的联通区域内节点个数
例1:
输入:
ConnectingGraph2(5)
query(1)
connect(1, 2)
query(1)
connect(2, 4)
query(1)
connect(1, 4)
query(1)
输出:
[1,2,3,3]
例2:
输入:
ConnectingGraph2(6)
query(1)
query(2)
query(1)
query(5)
query(1)
输出:
[1,1,1,1,1]
'''

class ConnectingGraph2:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.treeSize = [1 for _ in range(n + 1)]
        self.count = n

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.treeSize[a] < self.treeSize[b]:
            self.parent[a] = b
            self.treeSize[b] += self.treeSize[a]
        else:
            self.parent[b] = a
            self.treeSize[a] += self.treeSize[b]
        self.count -= 1

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    """
    @param: a: An integer
    @return: An integer
    """
    def query(self, a):
        a = self.find(a)
        return self.treeSize[a]





