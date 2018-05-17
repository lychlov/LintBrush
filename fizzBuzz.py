# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     fizzBuzz
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
    @param n: An integer
    @return: A list of strings.
    """

    def fizzBuzz(self, n):
        # write your code here
        return [' '.join([value + 'zz' for key, value in {3: 'fi', 5: 'bu'}.items() if x % key == 0]) or str(x) for x in
                range(1, n+1)]
