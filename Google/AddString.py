class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return sum of num1 and num2
    """

    def addStrings(self, num1, num2):
        # write your code here
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        result = ""
        up = 0
        for i in range(len(num1)):
            if i < len(num2):
                digit = int(num2[-(i + 1)]) + int(num1[-(i + 1)]) + up
            else:
                digit = int(num1[-(i + 1)]) + up
            up = 1 if digit >= 10 else 0

            result += (str(digit)[-1])
        if up == 1:
            result += '1'
        result = result[::-1]
        return result


num1 = '123'
num2 = '45'
sol = Solution()
print(sol.addStrings(num1, num2))
