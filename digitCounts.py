# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     digitCounts
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
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k, n):
        # write your code here
        count = 0
        k = str(k)
        for i in range(n + 1):
            count += str(i).count(k)
        return count


sol = Solution()
print(sol.digitCounts(1, 1))
