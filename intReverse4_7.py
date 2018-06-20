class Solution:
    def int_reverse_4_7(self, n):
        if n < 999999:
            print("this int does not have 7 digits..")
        temp = str(n)[::-1]
        return temp[3:7]


sol = Solution()
print(sol.int_reverse_4_7(1234567))
