import numpy as np
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 1
        cur_max = 0
        #idxs = np.argsort(position)
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort()
        stack = []
        
        for p, s in pair:
            stack.append((target-p)/s)
        
        for i in range(len(position)-1):
            cur_max = max(cur_max, stack[-1])
            stack.pop()
            if cur_max < stack[-1]:
                res += 1
        return res