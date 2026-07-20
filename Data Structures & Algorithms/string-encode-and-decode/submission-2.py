class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s))
            encoded_string += "#"
            encoded_string += s
        return encoded_string


    def decode(self, s: str) -> List[str]:
        num = ""
        decode_string = []
        pointer = 0
        while pointer < len(s):
            if s[pointer] == "#":
                pointer += 1
                decode_string.append(s[pointer: pointer+int(num)])
                pointer += int(num)
                num = ""
                continue
            num += s[pointer]
            pointer += 1
        return decode_string
