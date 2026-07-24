import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+': operator.add, 
                    '-': operator.sub, 
                    '*': operator.mul, 
                    '/': operator.truediv}

        for token in tokens:
            if token in operators.keys():
                val1 = stack.pop()
                val2 = stack.pop()
                print(token)
                print(val1, val2)
                stack.append(int(operators[token] (val2, val1)))
            else:
                stack.append(int(token))
        
        return stack[0]