# Solution 1
class Solution:

    def sortedSquares(self, nums):
        for index, value in enumerate(nums):
            nums[index] = value * value
        return sorted(nums)

# Solution 2


class Solution:

    def sortedSquares(self, nums):
        for index, value in enumerate(nums):
            nums[index] = value ** 2
        return sorted(nums)


List = [-10, -1, 1, 2, 3, 4]
print(Solution().sortedSquares(List))
