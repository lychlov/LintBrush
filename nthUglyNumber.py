# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     nthUglyNumber
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
    @param n: An integer
    @return: the nth prime number as description.
    """

    def nthUglyNumber(self, n):
        # write your code here
        ugly_num = [1]
        index = 0
        dict_pow = {2: 0, 3: 0, 5: 0}
        while index < n:
            temp2 = ugly_num[dict_pow[2]] * 2
            temp3 = ugly_num[dict_pow[3]] * 3
            temp5 = ugly_num[dict_pow[5]] * 5
