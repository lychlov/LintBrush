class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """

    def isToeplitzMatrix(self, matrix):
        # Write your code here
        temp = matrix[0][0]
        path = min(len(matrix), len(matrix[0]))
        for i in range(path):
            if temp != matrix[i][i]:
                return False
        return True


matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
sol = Solution()
print(sol.isToeplitzMatrix(matrix))
