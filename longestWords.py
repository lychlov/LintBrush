# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     longestWords
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
    @param: dictionary: an array of strings
    @return: an arraylist of strings
    """

    def longestWords(self, dictionary):
        # write your code here
        temp_list = []
        temp_max = 0
        for word in dictionary:
            if len(word) > temp_max:
                temp_max = len(word)
                temp_list = [word]
            elif len(word) == temp_max:
                temp_list.append(word)
        return temp_list


sol = Solution()
print(sol.longestWords(["dog", "google", "facebook", "internationalization", "blabla"]))
