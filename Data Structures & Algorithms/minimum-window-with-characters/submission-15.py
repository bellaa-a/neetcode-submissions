class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""

        if len(t) > len(s):
            return res
        
        res_min = len(s)
        l = 0
        t_count = {}
        s_count = {}
        have_count = 0
        for char in t:
            t_count[char] = 1 + t_count.get(char, 0)
        need_count = len(t_count)

        for r in range(len(s)):
            if s[r] in t_count.keys():
                s_count[s[r]] = 1 + s_count.get(s[r], 0)
                if s_count[s[r]] == t_count[s[r]]:
                    have_count += 1
            while have_count >= need_count:
                if s[l] in t_count.keys():
                    s_count[s[l]] -= 1
                    if s_count[s[l]] < t_count[s[l]]:
                        have_count -= 1

                if len(s[l:r+1]) <= res_min:
                    res = s[l:r+1]
                    res_min = len(s[l:r+1])
                l += 1
        
        return res