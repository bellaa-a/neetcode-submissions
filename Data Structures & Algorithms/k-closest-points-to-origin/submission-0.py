class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        min_heap = []
        dict_map = defaultdict(list)
        for point in points:
            x1 = point[0]
            y1 = point[1]
            dist = math.sqrt(x1 * x1 + y1 * y1)
            dict_map[dist].append(point)
        
        for key in dict_map:
            heapq.heappush(min_heap, key)
        
        
        while len(res) < k:
            for point in dict_map[heapq.heappop(min_heap)]:
                if len(res) >= k:
                    return res
                res.append(point)
        
        return res