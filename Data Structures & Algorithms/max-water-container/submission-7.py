class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        idx = 0
        jdx = len(heights) - 1
        for k in range(len(heights)):
            # print ("idx,jdx:",idx,jdx)
            max_area = max((min(heights[idx],heights[jdx]) * (jdx-idx)),max_area)
            if idx == jdx:
                return max_area
            elif heights[idx] <= heights[jdx]: # left increment
                idx += 1
            else: # right decrement
                jdx -= 1

        # max_area = 0
        # length = len(heights)
        # for idx,i in enumerate(heights):
        #     for jdx in range(length):
        #         new_jdx = len(heights) - jdx-1
        #         j = heights[new_jdx]
        #         max_area = max((min(i,j) * (new_jdx-idx)),max_area)
        #     length -= 1
        # return max_area

        
        # max_area = 0
        # length = len(heights)
        # left_flag = False
        # right_flag = 0
        # for idx,i in enumerate(heights):
        #     jdx = length - right_flag - 1
        #     j = heights[jdx]
        #     max_area = max((min(i,j) * (jdx-idx)),max_area)
        #     if (i < j): left_flag = True
        #     else: right_flag += 1
        # return max_area


