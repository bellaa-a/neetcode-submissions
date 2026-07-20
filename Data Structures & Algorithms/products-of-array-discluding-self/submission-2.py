class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product = 1
        # zero_count = 0
        # result = []
        # for num in nums:
        #     if num == 0:
        #         zero_count += 1
        #         continue
        #     product *= num

        # if zero_count >= 2:
        #     return [0] * len(nums)

        # if zero_count == 1:
        #     for num in nums:
        #         if num == 0:
        #             result.append(product)
        #         elif 0 in nums:
        #             result.append(0)
        #     return result

        # for num in nums:
        #     result.append(int(product / num))

        # return result
        result = [0] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result