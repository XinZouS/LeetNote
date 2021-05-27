'''
🍊1849. 爱生气的书店老板
中等  https://www.lintcode.com/problem/1849/
有一个书店，在接下来的n天中的第ii天会有customer[i]个顾客到来，并且在这一天结束后离开。
但是书店老板的脾气时好时坏，我们用一个数组grumpy表示他每一天的脾气好坏，若grumpy[i]=1, 则表示第 i 天老板的脾气很不好；若 grumpy[i]=0, 则表示第 i 天老板的脾气很好。
若某一天书店老板的脾气不好，则会导致所有当天来的所有顾客会给书店差评。但如果某一天脾气好，那么当天所有顾客都会给书店好评。
老板想要尽量增加给书店好评的人数数量，想了一个方法。他可以保持连续X天的好脾气。但这个方法只能使用一次。
那么在这n天这个书店最多能有多少人离开时给书店好评？

样例 1:
输入:
[1,0,1,2,1,1,7,5]
[0,1,0,1,0,1,0,1]
3
输出: 16
解释: 
书店老板在最后3天保持好脾气。感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.

'''
# python key
# 先要计算不做更新时原本能得多少分result，因为有可能是最大结果，并把前X天加入result窗口；
# 然后看评分为0的那些天（即grumpy[i] == 1），把分加进result，进行滑窗：
class Solution:
    """
    @param customers: the number of customers
    @param grumpy: the owner's temper every day
    @param X: X days
    @return: calc the max satisfied customers
    """
    def maxSatisfied(self, customers, grumpy, X):
        if not customers or not grumpy:
            return 0
        sumScore = 0
        n = len(customers)
        for i in range(n):
            if i < X:
                sumScore += customers[i]
            else:
                sumScore += customers[i] if grumpy[i] == 0 else 0
        l, r = 0, X
        res = sumScore
        while r < n:
            if grumpy[r] == 1:
                sumScore += customers[r]
            if grumpy[l] == 1:
                sumScore -= customers[l]
            res = max(res, sumScore)
            l += 1
            r += 1
        return res

