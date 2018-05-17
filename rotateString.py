# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     rotateString
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
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """

    def rotateString(self, str, offset):
        # write your code here
        offset = len(str) - offset % len(str)
        temp_a = str[:offset]
        temp_b = str[offset:]
        return temp_b + temp_a


sol = Solution()
print(sol.rotateString("abcdefg", 3))
