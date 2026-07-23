class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = collections.deque()
        res = []
        l=0
   
        for r in range(len(nums)):
            while window and nums[r] >= nums[window[-1]]:
                window.pop()
            window.append(r)

            while window[0] < l:
                window.popleft()

            if r >= k-1:
                res.append(nums[window[0]])
                l += 1
    
        return res