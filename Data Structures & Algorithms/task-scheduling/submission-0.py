class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        freq = {}
        heap = []
        queue = deque([])
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        for char, num in freq.items():
            heapq.heappush(heap, (-num, char))
        
        while heap or queue:
            while queue and queue[0][1] < res:
                heapq.heappush(heap, (queue[0][2], queue[0][0]))
                queue.popleft()

            if heap: 
                top = heapq.heappop(heap)
                new_num = top[0]+1
                if new_num != 0: queue.append((top[1], res+n, new_num))

            res += 1
        
        return res