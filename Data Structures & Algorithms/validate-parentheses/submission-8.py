class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []
        bracket_dict = {')':'(', '}':'{', ']':'['}

        for char in s:
            print(bracket_stack)
            if char in bracket_dict.values():
                bracket_stack.append(char)
            else:
                if bracket_stack == []:
                    return False
                
                if bracket_dict[char] != bracket_stack[-1]:
                        return False

                bracket_stack.pop()
        
        return bracket_stack == []