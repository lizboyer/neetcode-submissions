class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        left_idx = 0
        right_idx = len(nums) - 1

        for i in range(len(nums)):
            print("l,r:", nums[left_idx], nums[right_idx])
            print("idx l,r:", left_idx, right_idx)
            print(nums[left_idx + (right_idx - left_idx) //2])
            if nums[left_idx + (right_idx - left_idx) //2] > nums[(left_idx + (right_idx - left_idx) //2) + 1]:
                print("correct right")
                return(nums[(left_idx + (right_idx - left_idx) //2) + 1])

            if nums[left_idx] < nums[left_idx - 1]:
                print("correct left")
                return(nums[left_idx])
            if nums[right_idx] < nums[left_idx + (right_idx - left_idx) //2]: # if we need to move right
                print("right")
                left_idx = left_idx + (right_idx - left_idx) //2
            else: # if we need to move left
                print("left")
                right_idx = left_idx + (right_idx - left_idx) //2
        return 0