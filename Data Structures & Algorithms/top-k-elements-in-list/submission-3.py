class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict = {1: 1 time, 3: 2 times...}
        # result = [] x k
        num_dict = {}
        result = []
        for idx,val in enumerate(nums):
            cur_times = num_dict.get(val, 0)
            num_dict[val] = cur_times + 1
        print(num_dict)

        for i in range(k):
            max_val = 0
            idx_val = 0
            for idx,val in enumerate(num_dict):
                print(val, num_dict.get(val), max_val)
                if num_dict.get(val) > max_val:
                    print("ping")
                    max_val = num_dict.get(val)
                    idx_val = val
            result.append(idx_val) # put max_val into result
            print("res:", result)
            del num_dict[idx_val]
        return result