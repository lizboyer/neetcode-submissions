class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        left_idx = 0
        right_idx = len(nums) - 1

        for i in range(len(nums)):
            half = left_idx + (right_idx - left_idx) //2
            if nums[half] > nums[(half) + 1]:
                return(nums[(half) + 1])

            if nums[left_idx] < nums[left_idx - 1]:
                return(nums[left_idx])

            if nums[right_idx] < nums[half]: # if we need to move right
                left_idx = half

            else: # if we need to move left
                right_idx = half
        return 0