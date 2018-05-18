# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     randomSum
   Description :
   Author :       Lychlov
   date：          2018/5/18
-------------------------------------------------
   Change Activity:
                   2018/5/18:
-------------------------------------------------
"""
import random
import requests


class Solution:
    """
    @return: A new sorted integer array
    """

    def __init__(self):
        self.index = 1

    def randomSum(self, score):
        count = {0: 0, 1: 0, 2: 0, 3: 0}
        for i in range(score):
            count[random.randint(0, 3)] += 1
        base_url ='http://223.105.5.74:8000/projectvote/tool/search.php?opt=3&a=%s&b=%s&c=%s&d=%s&project=%s&telNo=15939049399&jtype=1' % \
                   (count[0], count[1], count[2], count[3], self.index)
        self.index += 1
        requests.get(base_url)
        return base_url
