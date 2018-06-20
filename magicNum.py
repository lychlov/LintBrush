class Solution:
    def magic_num(self):
        for h_dig in range(1, 5):
            for t_dig in range(1, 5):
                if h_dig == t_dig:
                    continue
                for dig in range(1, 5):
                    if dig == h_dig or dig == t_dig:
                        continue
                    print(h_dig, t_dig, dig)


sol = Solution()
sol.magic_num()
