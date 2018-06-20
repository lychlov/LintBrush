class Solution:
    def abc_vs_xyz(self):
        xyz = {0: 'x', 1: 'y', 2: 'z'}
        for a in range(3):
            for b in range(3):
                if a == b:
                    continue
                for c in range(3):
                    if a == c or b == c:
                        continue
                    if a == 0 or c == 0 or c == 2:
                        continue
                    print("a vs %s\nb vs %s\nc vs %s\n" % (xyz[a], xyz[b], xyz[c]))


sol = Solution()
sol.abc_vs_xyz()
