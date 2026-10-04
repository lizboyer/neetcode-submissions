class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_idx = 0
        right_idx = len(nums) - 1

        for i in range(len(nums)):
            half = left_idx + (right_idx - left_idx) //2
            # print("half:", nums[half])
            # print("l,r:", nums[left_idx], nums[right_idx])

            if nums[half] == target:
                return half
            elif nums[right_idx] == target:
                return right_idx
            elif nums[left_idx] == target:
                return left_idx

            if nums[right_idx] < nums[half]: # if the zero's on the right
                if target > nums[half] or target < nums[right_idx]: # can the number be found on the left?
                    # print("wrap right, right")
                    left_idx = half

                else:
                    # print("wrap right, left")
                    right_idx = half

            else: # the zero's on the left
                if target > nums[half] and target < nums[right_idx]: # can the number be found on the left?
                    # print("wrap left, right")
                    left_idx = half
                    
                else:
                    # print("wrap left, left")
                    right_idx = half
        return -1