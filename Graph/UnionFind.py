'''
https://labuladong.gitbook.io/algo/gao-pin-mian-shi-xi-lie/unionfind-suan-fa-xiang-jie

'''

class UnionFind:
	# O(n)
	def __init__(self, n: int):
		self.count = n
		self.parent = [i for i in range(n)]
		self.treeSize = [1 for _ in range(n)]

	# O(1)
	def union(self, a: int, b: int) -> int:
		pA = self._find(a)
		pB = self._find(b)
		if pA == pB:
			return pA
		if self.treeSize[pA] < self.treeSize[pB]:
			self.parent[pA] = pB
			self.treeSize[pB] += self.treeSize[pA]
		else:
			self.parent[pB] = pA
			self.treeSize[pA] += self.treeSize[pB]
		self.count -= 1
		return pA

	# O(1)
	def _find(self, a: int) -> int:
		if a >= len(self.parent): return -1
		while a != self.parent[a]:
			self.parent[a] = self.parent[self.parent[a]]
			a = self.parent[a]
		return a

	def isConnected(self, a: int, b: int) -> bool:
		a = self._find(a)
		b = self._find(b)
		return a == b

	# O(1)
	def count(self) -> int:
		return self.count

