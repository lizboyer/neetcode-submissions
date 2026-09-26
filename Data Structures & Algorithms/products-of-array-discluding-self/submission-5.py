class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # multiply all items that are not zero
        multiplicand = 0
        zero_flag = False
        many_zeros_flag = False
        for idx,value in enumerate(nums):
            if value != 0:
                if multiplicand == 0:
                    multiplicand += 1
                multiplicand = multiplicand * value
        # if there is a zero, zero_flag = true
            elif zero_flag == False:
                zero_flag = True
            else:
                many_zeros_flag = True


        # loop through and divide by i if zero_flag = false
        for i in range(len(nums)):
            print(nums[i])
            if zero_flag == False:
                nums[i] = multiplicand // nums[i]
                print(nums[i])
        # if zero_flag = true, AND nums[i] == 0, divide by 1
            elif nums[i] == 0:
                if many_zeros_flag:
                    print("hit")
                    nums[i] == 0
                else:
                    nums[i] = multiplicand
        # if zero_flag = true AND nums[i] != 0, item = 0
            else:
                nums[i] = 0
        return nums