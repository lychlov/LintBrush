class Solution:
    def rabbit_population(self, n):
        if n == 1 or n == 2:
            return 1
        else:
            return self.rabbit_population(n - 1) + self.rabbit_population(n - 2)


sol = Solution()
for i in range(1, 20):
    print(sol.rabbit_population(i))
