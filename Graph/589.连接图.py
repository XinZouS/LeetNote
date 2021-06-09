'''
Medium  https://www.lintcode.com/problem/589/
给一个图中的n个节点, 记为 1 到 n . 在开始的时候图中没有边。
你需要完成下面两个方法:
        1. connect(a, b), 添加连接节点 a, b 的边.
        2. query(a, b), 检验两个节点是否联通
例1:
输入:
ConnectingGraph(5)
query(1, 2)
connect(1, 2)
query(1, 3) 
connect(2, 4)
query(1, 4) 
输出:
[false,false,true]
例2:
输入:
ConnectingGraph(6)
query(1, 2)
query(2, 3)
query(1, 3)
query(5, 6)
query(1, 4)
输出:
[false,false,false,false,false]
'''

# python: UnionFind
class ConnectingGraph:
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
        n = len(self.parent)
        if not (0 <= a < n and 0 <= b < n):
            return 
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
        if not 0 <= x < len(self.parent):
            return x
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
        
    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    def query(self, a, b):
        return self.find(a) == self.find(b)






