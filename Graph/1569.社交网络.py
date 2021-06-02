'''
🍊🔐1569. 社交网络
中等  https://www.lintcode.com/problem/1569/
每个人都有自己的网上好友。现在有n个人，给出m对好友关系，寻问任意一个人是否能直接或者间接的联系到所有网上的人。若能，返回yes，若不能，返回no。好友关系用a数组和b数组表示，代表a[i]和b[i]是一对好友。

样例1									样例2
输入: n=4, a=[1,1,1], b=[2,3,4]			输入: n=5, a=[1,2,4], b=[2,3,5]
输出: "yes"								输出: "no"
说明:									Explanation:
1和2，3，4能直接联系							1，2，3能相互联系
2，3，4和1能直接联系，这3个人能通过1间接联系		4，5能相互联系
											不过这两组人不能联系，比如，1无法联系4或者5
'''

# python
class Solution:
    """
    @param n: the person sum
    @param a: the array a
    @param b: the array b
    @return: yes or no
    """
    class UnionFind:
        def __init__(self, n):
            self.parent = [i for i in range(n)]
            self.treeSize = [1 for _ in range(n)]
            self.count = n

        def union(self, a, b):
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

        def find(self, x) -> int:
            while x != self.parent[x]:
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x

        def isConnect(self, a, b) -> bool:
            return self.find(a) == self.find(b)

        def socialNetwork(self, n, a, b):
            if n <= 0:
                return 'no'
            uf = self.UnionFind(n + 1) # 1-based arr, so+ one '0'
            for i, j in zip(a, b):
                uf.union(i, j)
            return 'yes' if uf.count == 2 else 'no' # 1-based, so 0->0 add 1;

