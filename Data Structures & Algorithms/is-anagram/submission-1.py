class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for char in s:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
        seen2 = {}
        for char in t:
            if char in seen2:
                seen2[char] += 1
            else:
                seen2[char] = 1
        return (seen == seen2)