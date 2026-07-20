# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         encoded_string = ""
#         for s in strs:
#             encoded_string += str(len(s))
#             encoded_string += "#"
#             encoded_string += s
#         return encoded_string


#     def decode(self, s: str) -> List[str]:
#         num = ""
#         decode_string = []
#         found_pound = False
#         pointer = 0
#         while pointer < len(s):
#             if found_pound:
#                 decode_string.append(s[pointer: pointer+int(num)])
#                 pointer += int(num)
#                 num = ""
#                 found_pound = False
#                 continue
#             if s[pointer] == "#":
#                 found_pound = True
#                 pointer += 1
#                 continue
#             num += s[pointer]
#             pointer += 1
#         return decode_string

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
