class Solution:
    def magic_num2(self):
        for h_dig in range(1, 5):
            for t_dig in range(1, 5):
                for dig in range(1, 5):
                    if h_dig==t_dig or h_dig==dig or t_dig==dig:
                        continue
                    print(h_dig, t_dig, dig)


sol = Solution()
sol.magic_num2()
