class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here
        list_res = []
        length = len(nums)
        for i in range(length):
            res = [nums[i]]
            for j in range(length):
                if i == j:
                    break
                res.append(nums[j])
            list_res.append(res)
        return list_res


sol = Solution()
nums = [1, 2, 3]
print(sol.permute(nums))
