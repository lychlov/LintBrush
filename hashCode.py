# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     hashCode
   Description :
   Author :       Lychlov
   date：          2018/5/18
-------------------------------------------------
   Change Activity:
                   2018/5/18:
-------------------------------------------------
"""


class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """

    def hashCode(self, key, HASH_SIZE):
        # write your code here
        sum_all = 0
        for i in range(len(key)):
            sum_all = (sum_all * 33 + ord(key[i])) % HASH_SIZE
        return sum_all % HASH_SIZE


sol = Solution()
print(sol.hashCode('abcd', 100))
