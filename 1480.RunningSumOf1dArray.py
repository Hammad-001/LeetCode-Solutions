class Solution:

    def runningSum(self, nums):
        for index in range(1, len(nums)):
            nums[index] += nums[index - 1]
        return nums

List = [-1, 0, 3, 5, 9, 12]
print(Solution().runningSum(List))
