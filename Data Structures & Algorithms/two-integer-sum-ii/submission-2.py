class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for idx,i in enumerate(numbers):
            dict[i] = idx
        for idx,i in enumerate(numbers):
            if dict.get(target - i) and dict.get(target - i) != idx:
                j = dict.get(target - i)
                return([min(idx+1,j+1),max(idx+1,j+1)])