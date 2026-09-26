class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        result = []
        for idx,val in enumerate(nums):
            cur_times = num_dict.get(val, 0)
            num_dict[val] = cur_times + 1

        for i in range(k):
            max_val = 0
            idx_val = 0
            for idx,val in enumerate(num_dict):
                if num_dict.get(val) > max_val:
                    max_val = num_dict.get(val)
                    idx_val = val
            result.append(idx_val) # put max_val into result
            del num_dict[idx_val]
        return result