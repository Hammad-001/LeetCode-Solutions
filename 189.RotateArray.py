# # Solution 1
# class Solution:
#     def rotate(self, nums, k):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(k):
#             nums.insert(0, nums[-1])
#             nums.pop()

# Solution 2
# Time Limit exceeded
# class Solution:

#     def rotate(self, nums, k):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(k):
#             temp = nums[-1]
#             for index in range(len(nums) - 1, -1, -1):
#                 nums[index] = nums[index - 1]
#             nums[0] = temp
#         print(nums)

# Solution 3
class Solution:

    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        left = nums[len(nums)-k % len(nums):]
        right = nums[:len(nums)-k % len(nums)]
        nums[:] = left + right
        print(nums)

List = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate(List, 3)
