class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""

        if len(t) > len(s):
            return res
        
        res_min = len(s)
        l = 0
        t_count = {}
        s_count = {}
        for char in t:
            t_count[char] = 1 + t_count.get(char, 0)

        for r in range(len(s)):
            if s[r] in t_count.keys():
                s_count[s[r]] = 1 + s_count.get(s[r], 0)
            while s_count.keys() == t_count.keys() and all(s_count[k] >= t_count[k] for k in s_count):
                if s[l] in t_count.keys():
                    s_count[s[l]] -= 1

                if len(s[l:r+1]) <= res_min:
                    res = s[l:r+1]
                    res_min = len(s[l:r+1])
                l += 1
        
        return res