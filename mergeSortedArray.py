# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     mergeSortedArray
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
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """

    def mergeSortedArray(self, A, B):
        # write your code here
        if len(A) >= len(B):
            for b in B:
                A.append(b)
            A.sort()
            return A
        else:
            for a in A:
                B.append(a)
            B.sort()
            return B


sol = Solution()
print(sol.mergeSortedArray([1, 2, 3, 4], [2, 4, 5]))
