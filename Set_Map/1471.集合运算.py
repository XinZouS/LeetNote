'''
🍏1471. 集合运算
简单   https://www.lintcode.com/problem/1471/
给定两个集合A,B，分别输出A和B的并集、交集和差集的大小
	• 集合的大小不超过1e6
	• 集合中出现的数值大小不超过1e6
样例1
输入: A = [1,3,4,6] 和 B = [1,5,10]
输出: [6,1,3]
解释: 
A,B的并集、交集和差集分别为：[1,3,4,5,6,10]、[1]、[3,4,6]
对应的集合大小为：6、1、3

样例2
输入: A = [1,2,3] 和 B = [4,5,6]
输出: [6,0,3]
解释: 
A,B的并集、交集和差集分别为：[1,2,3,4,5,6]、[]、[1,2,3]
对应的集合大小为：6、0、3

'''

# python
class Solution:
    """
    @param A: The set A
    @param B: The set B
    @return: Return the size of three sets
    """
    def getAnswer(self, A, B):
        setA, setB = set(A), set(B)
        union = setA.union(setB)
        inter = setA.intersection(setB)
        diffe = setA.difference(setB)
        return [len(union), len(inter), len(diffe)]


