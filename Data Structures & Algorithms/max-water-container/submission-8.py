class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        idx = 0
        jdx = len(heights) - 1
        for k in range(len(heights)):
            max_area = max((min(heights[idx],heights[jdx]) * (jdx-idx)),max_area)
            if idx == jdx:
                return max_area
            elif heights[idx] <= heights[jdx]: # left increment
                idx += 1
            else: # right decrement
                jdx -= 1


