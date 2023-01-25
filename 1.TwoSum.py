# Solution 1
class Solution:

    def twoSum(self, nums, target: int):
        for index1, value1 in enumerate(nums):
            for index2, value2 in enumerate(nums):
                if index1 != index2:
                    if value1 + value2 == target:
                        return [index1, index2]

# # Solution 2
# class Solution:

#     def twoSum(self, nums, target):
#         val = {}
#         for i in range(len(nums)):
#             if target - nums[i] in val:
#                 return [i, val[target - nums[i]]]
#             val[nums[i]] = i

print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
