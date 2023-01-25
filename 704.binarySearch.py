class Solution:

    def search(self, nums, target):
        start = 0
        end = len(nums)

        found = False

        mid = end // 2

        for i in range(len(nums)):
            print(nums[mid], start,mid, end, "G:" + str(nums[mid] > target), target)

            if nums[mid] == target:
                found = True
                break

            if nums[mid] < target:
                start = mid
                mid = (start + end) // 2

            if nums[mid] > target:
                end = mid
                mid = (start + end) // 2

        if not found:
            return -1

        return mid

List = [-1, 0, 3, 5, 9, 12]
print(Solution().search(List, 3))
