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
        index_reg = [0] * 3
        ugly_nums = [1]
        while len(ugly_nums) < n:
            temp = {ugly_nums[index_reg[key]] * value: key for key, value in {0: 2, 1: 3, 2: 5}.items()}
            new_num = min(temp)
            if new_num>ugly_nums[-1]:
                ugly_nums.append(new_num)
            index_reg[temp[new_num]] += 1
        return ugly_nums[-1]


sol = Solution()
print(sol.nthUglyNumber(20))
