# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     rearrange
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
    @param str: a string containing uppercase alphabets and integer digits
    @return: the alphabets in the order followed by the sum of digits
    """
    def rearrange(self, str2):
        # Write your code here
        temp_str = []
        temp_sum = 0
        for d in str2:
            if d.isdigit():
                temp_sum += int(d)
            else:
                temp_str.append(d)
        temp_str.sort()
        return "".join(temp_str)+str(temp_sum if temp_sum else '')

sol = Solution()
print(sol.rearrange("AC2BEW3"))