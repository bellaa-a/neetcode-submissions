class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []

        for char in s:
            print(bracket_stack)
            if char == '(' or char == '{' or char == '[':
                bracket_stack.append(char)
            else:
                if bracket_stack == []:
                    return False

                if char == ')':
                    if '(' != bracket_stack[-1]:
                        return False
                elif char == '}':
                    if '{' != bracket_stack[-1]:
                        return False
                else:
                    if '[' != bracket_stack[-1]:
                        return False

                bracket_stack.pop()
        
        return bracket_stack == []