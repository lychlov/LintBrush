# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     trailingZeros
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
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """

    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        if n == 0: return 0
        return n // 5 + self.trailingZeros(n // 5)


sol = Solution()
print(sol.trailingZeros(105))
