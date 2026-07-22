class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1_arr = [0] * 26
        s2_arr = [0] * 26
        
        for char1 in s1:
            s1_arr[ord(char1) - ord('a')] += 1

        l = 1
        
        for i in range(len(s1)):
            s2_arr[ord(s2[i]) - ord('a')] += 1
        
        if s1_arr == s2_arr:
            return True

        for r in range(len(s1), len(s2)):
            s2_arr[ord(s2[l-1]) - ord('a')] -= 1
            s2_arr[ord(s2[r]) - ord('a')] += 1
            l += 1

            if s1_arr == s2_arr:
                return True
        
        return False
        