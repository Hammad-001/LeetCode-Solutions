class Solution:
    def maximumWealth(self, accounts):
        maxwealth = 0
        for i in accounts:
            wealth = 0
            for j in i:
                wealth += j
            if wealth > maxwealth:
                maxwealth = wealth
        return maxwealth

List = [[1,2,3],[3,2,1]]
print(Solution().maximumWealth(List))