class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        result = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        
        for n, freq in count.items():
            bucket[freq].append(n)

        for i in range(len(nums), 0, -1):
            for n in bucket[i]:
                result.append(n)
                if len(result) == k:
                    return result
        