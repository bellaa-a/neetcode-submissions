class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        for char_s in s:
            if char_s not in s_dict.keys():
                s_dict[char_s] = 1
            else:
                s_dict[char_s] += 1
        
        t_dict = {}
        for char_t in t:
            if char_t not in t_dict.keys():
                t_dict[char_t] = 1
            else:
                t_dict[char_t] += 1
         
        for key_s in s_dict.keys():
            if key_s not in t_dict.keys():
                return False
            if s_dict[key_s] != t_dict[key_s]:
                return False
        
        # for key_t in t_dict.keys():
        #     if key_t not in s_dict.keys():
        #         return False
        #     if s_dict[key_t] != t_dict[key_t]:
        #         return False

        return True
        