'''
🍊1070 · 账户合并
中等  https://www.lintcode.com/problem/1070/
给定一个帐户列表，每个元素accounts [i]是一个字符串列表，其中第一个元素accounts [i] [0]是账户名称，其余元素是这个帐户的电子邮件。
现在，我们想合并这些帐户。
如果两个帐户有相同的电子邮件地址，则这两个帐户肯定属于同一个人。
请注意，即使两个帐户具有相同的名称，它们也可能属于不同的人，因为两个不同的人可能会使用相同的名称。
一个人可以拥有任意数量的账户，但他的所有帐户肯定具有相同的名称。
合并帐户后，按以下格式返回帐户：每个帐户的第一个元素是名称，其余元素是按字典序排序后的电子邮件。
帐户本身可以按任何顺序返回。
账户个数在1-1000之间
每个账户下的电子邮件在1-10之间
每个字符串的长度在1~30之间

样例
输入:
	[
		["John", "johnsmith@mail.com", "john00@mail.com"],
		["John", "johnnybravo@mail.com"],
		["John", "johnsmith@mail.com", "john_newyork@mail.com"],
		["Mary", "mary@mail.com"]
	]
	
输出: 
	[
		["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
		["John", "johnnybravo@mail.com"],
		["Mary", "mary@mail.com"]
	]
解释: 
	第一个第三个John是同一个人的账户，因为这两个账户有相同的邮箱："johnsmith@mail.com".
	剩下的两个账户分别是不同的人。因为他们没有和别的账户有相同的邮箱。
你可以以任意顺序返回结果。比如：
	
	[
		['Mary', 'mary@mail.com'],
		['John', 'johnnybravo@mail.com'],
		['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']
	]
	也是可以的。

'''

# python key:  UnionFind
class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """
    def accountsMerge(self, accounts):
        # 1. {'email': [1,2,5]}
        self.email2Ids = self.getEmail2Ids(accounts)
        # 2.
        self.initUnionFind(len(accounts))
        # 3. union userId
        for email, ids in self.email2Ids.items():
            root = ids[0]
            for userId in ids[1:]:
                self.union(root, userId)
        # 4. merge
        return self.getName2Emails()

    def getEmail2Ids(self, accounts) -> dict:
        self.id2Name = dict()
        email2Ids = dict()
        for userId, info in enumerate(accounts):
            userName = info[0]
            self.id2Name[userId] = userName
            for e in info[1:]:
                if e in email2Ids:
                    email2Ids[e].append(userId)
                else:
                    email2Ids[e] = [userId]
        return email2Ids

    def getName2Emails(self):
        id2Emails = dict() # {id: [e1,e2]}
        for email, ids in self.email2Ids.items():
            for userId in ids: # MUST check each userId
                userId = self.find(userId)
                if userId in id2Emails:
                    id2Emails[userId].add(email)
                else:
                    id2Emails[userId] = set([email]) # MUST remove duplicate email
        #
        result = []
        for userId, emails in id2Emails.items():
            rootUser = self.find(userId)
            userName = self.id2Name[rootUser]
            result.append([userName, *sorted(emails)])
        return result

    def initUnionFind(self, n):
        self.parent = [i for i in range(n)]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        self.parent[b] = a

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

