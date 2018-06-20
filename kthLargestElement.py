class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        A.sort()
        return A[len(A)-k]

A=[9,3,2,4,8]
sol=Solution()
print(sol.kthLargestElement(3,A))