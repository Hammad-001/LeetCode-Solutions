# # Solution 1
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         longest = 0
#         for i in range(len(s)):
#             length = 0
#             index = i
#             characters = []
#             while index < len(s):
#                 if s[index] not in characters:
#                     length +=1
#                     characters.append(s[index])
#                     index += 1
#                 else:
#                     break
#             if length > longest:
#                 longest = length
#         return longest

# Solution 2
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_string = ""
        length = 0
        for val in s:
            if val in my_string:
                my_string = my_string.split(val)[1] + val
                continue
            else:
                my_string += val
            length = max(len(my_string), length)
        return length
        

print(Solution().lengthOfLongestSubstring("abccbcadf"))