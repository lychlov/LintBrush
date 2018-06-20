class Solution:
    def factorial_sum(self):
        factorial=1
        sum=0
        for i in range(1,21):
            factorial=factorial*i
            sum+=factorial
        print("1!+...20!=%s"%sum)

sol = Solution()
sol.factorial_sum()