class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l < r:
            if numbers[r] + numbers[l] > target:
                r -= 1
                continue
            if numbers[r] + numbers[l] == target:
                return [l+1, r+1]
            l += 1