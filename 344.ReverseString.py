# # Solution 1
# class Solution:
#     def reverseString(self, s):
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         s[:] = s[::-1]
#         print(s)

# Solution 2
class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
        print(s)

Solution().reverseString(["h", "e", "l", "l", "0"])