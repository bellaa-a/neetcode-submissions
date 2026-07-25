class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        l = 0
        r = len(self.timemap[key])-1
        
        while l <= r:
            m = l + int((r-l)/2)
            val, t = self.timemap[key][m]
            if t == timestamp:
                return val
            elif t < timestamp:
                res = val
                l = m+1
            else:
                r = m-1
        
        return res


