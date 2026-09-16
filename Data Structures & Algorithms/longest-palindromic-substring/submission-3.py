class Solution:
    def longestPalindrome(self, s: str) -> str:
        d= ""
        m = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):  # Include the full string length
                sub = s[i:j]
                if sub == sub[::-1] and len(sub) > m:
                    m = len(sub)
                    d = sub
        return d