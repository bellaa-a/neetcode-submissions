class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for s in strs:
            str_list = [0] * 26
            for char in s:
                str_list[ord(char) - ord('a')] += 1
            anagram[tuple(str_list)].append(s)
        return list(anagram.values())