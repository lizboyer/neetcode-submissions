class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        if len(nums) <= 1:
            return False
        for i in nums:
            if hash.get(i, 0) != 0:
                return True
            hash[i] = 1
        return False