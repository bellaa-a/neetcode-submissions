import numpy as np
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 1
        cur_max = 0
        idxs = np.argsort(position)
        stack = []
        
        for i in idxs:
            stack.append((target-position[i])/speed[i])
        
        for i in range(len(idxs)-1):
            cur_max = max(cur_max, stack[-1])
            stack.pop()
            if cur_max < stack[-1]:
                res += 1
        return res