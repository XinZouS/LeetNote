'''
🍏128. 哈希函数

简单  https://www.lintcode.com/problem/128/description
在数据结构中，哈希函数是用来将一个字符串（或任何其他类型）转化为小于哈希表大小且大于等于零的整数。一个好的哈希函数可以尽可能少地产生冲突。一种广泛使用的哈希函数算法是使用数值 33，假设任何字符串都是基于 33 的一个大整数，比如：

其中HASH_SIZE表示哈希表的大小(可以假设一个哈希表就是一个索引 00 ~ HASH_SIZE - 1的数组)。给出一个字符串作为 key 和一个哈希表的大小，返回这个字符串的哈希值。
对于这个问题你不需要自己设计hash算法，你只需要实现上述描述的hash算法即可。
对于这个问题，您没有必要设计自己的哈希算法或考虑任何冲突问题，您只需要按照描述实现算法.
0 <= len(key) <= 1000000<=len(key)<=100000
样例 1:
输入:  key = "abcd", size = 1000
输出: 978	
样例解释：(97 * 33^3 + 98*33^2 + 99*33 + 100*1)%1000 = 978
样例 2:
输入:  key = "abcd", size = 100
输出: 78	
样例解释：(97 * 33^3 + 98*33^2 + 99*33 + 100*1)%100 = 78

'''

# python key:
class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """
    # 取模过程要使用 同余定理：(a * b ) % MOD = ((a % MOD) * (b % MOD)) % MOD
    def hashCode(self, key, HASH_SIZE):
        if not key:
            return HASH_SIZE
        n = len(key)
        if n == 1:
            return ord(key) % HASH_SIZE
            
        res = 0
        for c in key:
            res = (res * 33 + ord(c)) % HASH_SIZE
        return res

	   # My code TLE:
        # sums = ord(key[n - 1])
        # i = n - 2
        # pwr = 33
        # while i >= 0:
        #     sums += (ord(key[i]) + sums * pwr) % HASH_SIZE
        #     # pwr *= 33
        #     i -= 1
        # return sums % HASH_SIZE



