class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            one = heapq.heappop(max_heap)
            two = heapq.heappop(max_heap)
            new_val = -abs(one-two)
            if new_val != 0:
                heapq.heappush(max_heap, new_val)

        if max_heap:
            return -max_heap[0]
        else:
            return 0