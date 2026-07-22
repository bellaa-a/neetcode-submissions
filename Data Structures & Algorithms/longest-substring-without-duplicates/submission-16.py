class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        length = 0
        seen = {}
        for r in range(len(s)):
            if s[r] in seen.keys() and seen[s[r]] >= l:
                length -= seen[s[r]] - l
                l = seen[s[r]] + 1
            else:
                length += 1
                max_len = max(max_len, length)
            seen[s[r]] = r

        return max_len
        