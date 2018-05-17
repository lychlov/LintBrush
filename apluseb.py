# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     apluseb
   Description :
   Author :       Lychlov
   date：          2018/5/17
-------------------------------------------------
   Change Activity:
                   2018/5/17:
-------------------------------------------------
"""


class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b 
    """

    def aplusb(self, a, b):
        # write your code here
        return sum([a,b])


sol = Solution()
print(sol.aplusb(100, -100))
