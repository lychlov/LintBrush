class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """

    def generatePossibleNextMoves(self, s):
        # write your code here
        result = []
        if len(s) <= 1:
            return []
        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1] == '+':
                change = '-'
                temp = s[:i] + change * 2 + s[i + 2:]
                result.append(temp)
        return result


s = "++++"
sol = Solution()
print(sol.generatePossibleNextMoves(s))
