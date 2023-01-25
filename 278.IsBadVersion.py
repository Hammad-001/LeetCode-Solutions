class Solution:

    def firstBadVersion(self, n):
        start = 0
        end = n + 1
        first_bad = None
        for i in range(end):

            mid = (start + end) // 2

            if isBadVersion(mid):
                first_bad = mid
                if isBadVersion(mid - 1) and (mid - 1 > 0):
                    end = mid
                    mid = (start + end) // 2
                else:
                    return first_bad
            else:
                start = mid
                mid = (start + end) // 2

print(Solution().firstBadVersion(1))
