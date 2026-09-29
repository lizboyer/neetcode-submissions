class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dict = {}
        new_dict = {}
        return_val = []
        for idx,i in enumerate(nums):
            dict[i] = idx
        for idx,i in enumerate(nums):
            target = i
            for idx_j,j in enumerate(nums):
                if idx_j != idx:
                    if dict.get(-i-j) and dict.get(-i-j) != idx and dict.get(-i-j) != idx_j: # if k is in the list, and none are the same index
                        tmp = [i,j,-i-j]
                        tmp.sort()
                        # if new_dict[''.join(tmp)] != 1:
                        #     new_dict[''.join(tmp)] = 1
                        if new_dict.get(str(tmp)) != 1:
                            new_dict[str(tmp)] = 1
                            return_val.append(tmp)
        return(return_val)