class Solution:

    def searchInsert(self, nums, target):
        start = 0
        end = len(nums)
        for i in range(end):
            position = (start + end) // 2
            # print(position)

            if nums[position] == target:
                return position

            if nums[position] > target:
                end = position

            if nums[position] < target:
                start = position

        if nums[position] > target:
            if position > 0:
                return position - 1
            return position
        return position + 1

List = [-1, 0, 3, 5, 9, 12]
print(Solution().searchInsert(List, 2))
