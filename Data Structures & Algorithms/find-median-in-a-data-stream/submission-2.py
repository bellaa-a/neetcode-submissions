class MedianFinder:

    def __init__(self):
        self.left_half = [] # max heap
        self.right_half = [] # min heap

    def addNum(self, num: int) -> None:

        if self.right_half:
            if num < self.right_half[0]:
                heapq.heappush(self.left_half, -num)
            else:
                heapq.heappush(self.right_half, num)
        elif self.left_half:
            if num > -self.left_half[0]:
                heapq.heappush(self.right_half, num)
            else:
                heapq.heappush(self.left_half, -num)
        elif not self.right_half and not self.left_half:
             heapq.heappush(self.left_half, -num)


        while len(self.left_half) - len(self.right_half) > 1:
            value = heapq.heappop(self.left_half)
            heapq.heappush(self.right_half, -value)

        while len(self.right_half) - len(self.left_half) > 1:
            value = heapq.heappop(self.right_half)
            heapq.heappush(self.left_half, -value)


    def findMedian(self) -> float:
        if len(self.left_half) - len(self.right_half) == 1:
            return -self.left_half[0] 
        elif len(self.right_half) - len(self.left_half) == 1:
            return self.right_half[0]
        else:
            l = -self.left_half[0] if self.left_half else 0
            r = self.right_half[0] if self.right_half else 0
            return (l + r)/2