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
        ugly_nums = [1]
        index = 1
        dict_pow = [2, 3, 5]
        while index < n:
            candicated_list = []
            for ugly_num in ugly_nums[::-1]:
                flag = True
                temp =[ugly_num*power for power in dict_pow if ugly_num*power>ugly_nums[-1]]
                if len(temp)==0:
                    break
                candicated_list.append(min(temp))
            index += 1
            ugly_nums.append(min(candicated_list))
        return ugly_nums[-1]


sol = Solution()
print(sol.nthUglyNumber(20))
