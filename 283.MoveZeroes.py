# # Solution 1
# class Solution:
#     def moveZeroes(self, nums):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(nums.count(0)):
#             nums.remove(0)
#             nums.append(0)
#         return nums

# Solution 2


class Solution:

    def moveZeroes(self, nums):
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
        for i in range(index, len(nums)):
            nums[index] = 0
            index += 1
        return nums

print(Solution().moveZeroes([12, 3, 0, 6, 0, 0, 7, 8, 9]))
