class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        left = 0
        while True:
            left = nums[left]
            slow = nums[slow]
            if slow == left:
                return slow