class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        for c in s:
            if c.isalnum():
                l.append(c.lower())

        return l == l[::-1]