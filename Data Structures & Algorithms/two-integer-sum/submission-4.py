class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for index,value in enumerate(nums):
            for j in range(len(nums) - index):
                if (index != j+index) and value + nums[j + index] == target:
                    print("hit")
                    print("index,j:", index,j+index)
                    output.append(index)
                    output.append(j+index)
                    return output