"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def searchRange(self, root, k1, k2):
        # write your code here
        res = []
        self.search(res, root, k1, k2)
        return res

    def search(self, result, node, k1, k2):
        if node is None:
            return
        if node.val >= k1 and node.val <= k2:
            self.result.append(node.val)
        self.search(result, node.left, k1, k2)
        self.search(result, node.right, k1, k2)
