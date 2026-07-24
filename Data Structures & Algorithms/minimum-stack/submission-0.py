class MinStack:

    def __init__(self):
        self.stack = []
        self.cur_min = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.cur_min.append(min(val, self.cur_min[-1] if self.cur_min else val))
        

    def pop(self) -> None:
        self.stack.pop()
        self.cur_min.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.cur_min[-1]
        
