class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count, left, max_f = {}, 0, 0
        for right, char in enumerate(s):
            count[char] = count.get(char, 0) + 1
            max_f = max(max_f, count[char])
            if (right - left + 1) - max_f > k:
                count[s[left]] -= 1
                left += 1
        return len(s) - left
        # se=set(s)
        # ma=0
        # for i in se:
        #     if(s.count(i)>ma):
        #         ma=s.count(i)
        # if ma==len(s):
        #     return ma
        # return ma+k