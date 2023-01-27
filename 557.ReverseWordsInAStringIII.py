# # Solution 1
# # Reverse Words but not inplace in a string
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         words = s.split(" ")
#         for i in range(len(words)):
#             words[i] = words[i][::-1]
#         s = " ".join(map(str, words))
#         print(s)

class Solution:
    def reverseWords(self, s: str) -> str:
        print(" ".join([word[::-1] for word in s.split(" ")]))
        

Solution().reverseWords("Let's take LeetCode contest")