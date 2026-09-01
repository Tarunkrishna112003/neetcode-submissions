from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        req, win, l, ans = Counter(t), Counter(), 0, (float('inf'), 0, 0)
        have, need = 0, len(Counter(t))
        
        for r, c in enumerate(s):
            win[c] += 1
            if c in req and win[c] == req[c]: have += 1
            while have == need:
                ans = min(ans, (r - l + 1, l, r))
                if s[l] in req and win[s[l]] == req[s[l]]: have -= 1
                win[s[l]] -= 1; l += 1
                
        return s[ans[1]:ans[2]+1] if ans[0] != float('inf') else ""