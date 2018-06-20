class Solution:
    """
    @param A: An integer array
    @return: An integer
    """

    def singleNumber(self, A):
        # write your code here
        if len(A) == 0:
            return 0
        found = 0
        for a in A:
            found = found ^ a
        return found


sol = Solution()
A = [1, 1, 2, 2, 3, 4, 4]
print(bin(999))
print(sol.singleNumber(A))
