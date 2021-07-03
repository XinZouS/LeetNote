'''
🍎629 · 最小生成树

Saturday, July 3, 2021
3:15 PM

困难
给定一个Connections，即Connection类（边缘两端的城市名称和它们之间的开销），找到可以连接所有城市并且花费最少的边缘。
如果可以连接所有城市，则返回连接方法，否则返回空列表。
返回按成本排序的连接方法，或者如果其成本相同，就按照city1名称进行排序，如果city1名称也相同，则按照city2进行排序。

样例 1:
输入:
["Acity","Bcity",1]
["Acity","Ccity",2]
["Bcity","Ccity",3]
输出:
["Acity","Bcity",1]
["Acity","Ccity",2]

样例 2:
输入:
["Acity","Bcity",2]
["Bcity","Dcity",5]
["Acity","Dcity",4]
["Ccity","Ecity",1]
输出: []
解释: 没有办法连通
'''

'''
Definition for a Connection
class Connection:
def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost
'''
class Solution:
    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost(self, connections):
        import functools
        uf = self.UnionFind()
        for connection in connections:
            uf.add(connection.city1)
            uf.add(connection.city2)
        n, m = len(uf.parent), len(connections)
        connections.sort(key = functools.cmp_to_key(self.cmp))
        edges, mst = 0, []
        for connection in connections:
            if edges == n - 1:
                break
            city1, city2 = connection.city1, connection.city2
            if not uf.isConnect(city1, city2):
                uf.union(city1, city2)
                mst.append(connection) # 连接方法
                edges += 1
        
        if edges != n - 1:
            return []
        return mst
    def cmp(self, a, b):
        if a.cost != b.cost:
            return 1 if a.cost > b.cost else -1
        if a.city1 != b.city1:
            return 1 if a.city1 > b.city1 else -1
        if a.city2 != b.city2:
            return 1 if a.city2 > b.city2 else -1
        return 0 # a==b
    #
    class UnionFind:
        def __init__(self):
            self.parent = dict()
        
        def add(self, x):
            self.parent[x] = x
        def union(self, a, b):
            a = self.find(a)
            b = self.find(b)
            if a == b:
                return
            self.parent[b] = a
        def find(self, x):
            while x in self.parent and x != self.parent[x]:
                x = self.parent[x]
            return x
        
        def isConnect(self, a, b):
            return self.find(a) == self.find(b)

