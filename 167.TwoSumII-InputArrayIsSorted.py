# Solution 1
class Solution:
    def twoSum(self, numbers, target):
        diff = {}
        for index, value in enumerate(numbers):
            print(index, target-value, diff)
            if target-value in diff:
                return [diff[target-value]+1, index+1]
            diff[value] = index
                   

print(Solution().twoSum([0, 1,2,3,4,5,6,7], 9))