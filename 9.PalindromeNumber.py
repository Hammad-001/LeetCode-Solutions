# # Soultion 1
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         return str(x)==str(x)[::-1]

# Solution 2
class Solution:
    def isPalindrome(self, x: int) -> bool:
        for i in range(len(str(x))//2):
            if str(x)[i] != str(x)[len(str(x))-i-1]:
                return False
        return True

print(Solution().isPalindrome(100))