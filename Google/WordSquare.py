class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """

    def validWordSquare(self, words):
        # Write your code here
        k = 0
        while k < len(words):
            for i in range(k):
                try:
                    if words[k-i][k]==words[k][k-i]:
                        pass
                    else:
                        return False
                except:
                    return False
            k += 1
        return True


words = ["abcd", "bnrt", "crmy", "dtye"]
sol = Solution()
print(sol.validWordSquare(words))
