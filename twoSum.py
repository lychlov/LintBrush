# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     twoSum
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
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        # write your code here
        numbers.sort()
        n = len(numbers)
        for i in range(n):
            for j in range(i, n):
                temp = numbers[i] + numbers[j]
                if temp == target:
                    return [i, j]
                if temp > target:
                    break

sol = Solution()
print(sol.twoSum([2,7,11,15],9))