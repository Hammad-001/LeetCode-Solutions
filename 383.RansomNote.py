# Solution 1
class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False

        ransomNoteWords = dict()
        magzineWords = dict()

        for word in ransomNote:
            value = ransomNoteWords.get(word, None)
            if not value:
                ransomNoteWords[word] = 1
            else:
                ransomNoteWords[word] += 1
        
        for word in magazine:
            value = magzineWords.get(word, None)
            if not value:
                magzineWords[word] = 1
            else:
                magzineWords[word] += 1

        for key in ransomNoteWords.keys():
            value = magzineWords.get(key, None)
            if not value:
                return False
            if value < ransomNoteWords[key]:
                return False
        return True

# Solution 2
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False

        for i in set(ransomNote):
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True