class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        # write your code here
        ans = nums[0]
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum > ans:
                ans = sum
            if sum < 0:
                sum = 0
        return ans


sol = Solution()
# nums = [-4, 5, -4, 5, -4, 5, -4, 5, -4, 5, -4, 5, -4, 5, -4, 5, -4, 5, -1000]
nums=[-2,2,-3,4,-1,2,1,-5,3]
# nums = [-1, -2, -3, -100, -1, -50]

print(sol.maxSubArray(nums))
