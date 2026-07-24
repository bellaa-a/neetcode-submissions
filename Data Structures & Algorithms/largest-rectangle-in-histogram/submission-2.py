class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = [0] * len(heights)
        left = [0] * len(heights)
        right = [0] * len(heights)
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                left[i] += 1 + left[stack[-1]]
                stack.pop()
            stack.append(i)

        stack = []
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                right[i] += 1 + right[stack[-1]]
                stack.pop()
            stack.append(i)

        for i in range(len(heights)):
            res[i] = heights[i] * (left[i] + right[i] + 1)
        
        print(left)
        print(right)

        return max(res)