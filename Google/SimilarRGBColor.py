class Solution:
    """
    @param color: the given color
    @return: a 7 character color that is most similar to the given color
    """

    def similarRGB(self, color):
        # Write your code here
        list_dig = [color[1:3], color[3:5], color[5:7]]
        result = '#'
        for dig in list_dig:
            ori = int('0x%s' % dig, 16)
            similar = int(ori / 16)
            value = {
                (ori - (similar - 1) * 16 + similar - 1) ** 2: similar - 1,
                (ori - similar * 16 + similar) ** 2: similar,
                (ori - (similar + 1) * 16 + similar + 1) ** 2: similar + 1,
            }
            res = value[min(value)]
            if res == 16:
                res = res - 1
            result += hex(res)[-1]*2
        return result


color = '#09f166'
sol = Solution()
sol.similarRGB(color)
