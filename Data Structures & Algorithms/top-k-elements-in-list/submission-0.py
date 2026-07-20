class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        min_heap = []
        for key in count.keys():
            heapq.heappush(min_heap, [count[key], key])
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        for pair in min_heap:
            result.append(pair[1])
        
        return result

        