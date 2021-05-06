'''
Medium  https://leetcode.com/problems/lru-cache/
小齐讲解： https://mp.weixin.qq.com/s?__biz=MzIzNDQ3MzgxMw==&mid=2247483929&idx=1&sn=fda81057c47d376917ed142b2661f63a&chksm=e8f49223df831b35deb2e5316caddc241b4aa4bb58e8c66c906bdacfd695aca53aca86a5b173&scene=21
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
	• LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
	• int get(int key) Return the value of the key if the key exists, otherwise return -1.
	• void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
Follow up:
Could you do get and put in O(1) time complexity?
 
Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]
Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 
Constraints:
	• 1 <= capacity <= 3000
	• 0 <= key <= 3000
	• 0 <= value <= 104
	• At most 3 * 104 calls will be made to get and put.

'''

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dlist = self.Dlist()
        self.keys = dict()


    class Dnode:
        def __init__(self, key: int, val: int):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None
            

    class Dlist:
        def __init__(self):
            self.head = LRUCache.Dnode(0, 0)
            self.tail = LRUCache.Dnode(0, 0)
            self.size = 0
            self.head.next = self.tail
            self.tail.prev = self.head
            
        def insert(self, key: int, val: int) -> LRUCache.Dnode:
            xHead = self.head.next
            newNode = LRUCache.Dnode(key, val)
            self.head.next = newNode
            newNode.prev = self.head
            xHead.prev = newNode
            newNode.next = xHead
            self.size += 1
            return newNode
            
        def pop(self) -> int:
            if self.size == 0:
                return
            key = self.tail.prev.key
            pre = self.tail.prev.prev
            pre.next = self.tail
            self.tail.prev = pre
            self.size -= 1
            return key
        
        def update(self, node):
            if node.prev == self.head:
                return
            # pull it out
            nPrev, nNext = node.prev, node.next
            nPrev.next = nNext
            nNext.prev = nPrev
            # put it in
            hNext = self.head.next
            self.head.next = node
            hNext.prev = node
            node.prev = self.head
            node.next = hNext
        
            
    def get(self, key: int) -> int:
        if key in self.keys:
            node = self.keys[key]
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.dlist.update(self.keys[key])
        else:
            if self.dlist.size >= self.capacity:
                rmKey = self.dlist.pop()
                self.keys.pop(rmKey)
            node = self.dlist.insert(key, value)
            self.keys[key] = node


###### DEBUG ##############################################################

    def printCache(self):
        cur = self.dlist.head
        ls = list()
        while cur:
            ls.append('%i -> ' % cur.val)
            cur = cur.next
        print(self.keys.keys())
        print(ls)


s = LRUCache(3)
s.put(1,1)
s.printCache()
s.put(2,2)
s.printCache()
s.put(3,3)
s.printCache()
s.put(1,1)
s.printCache()
s.put(6,6)
s.printCache()
s.put(2,2)
s.printCache()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

