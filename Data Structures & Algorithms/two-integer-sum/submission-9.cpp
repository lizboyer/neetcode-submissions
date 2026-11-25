class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int look_for = 0;
        for(int i=0;i<nums.size();i++){
            look_for = target - nums[i];
            for(int j=0;j<nums.size();j++){
                if (nums[j] == look_for and j != i) {
                    vector<int> ret = {min(i,j), max(i,j)};
                    return(ret);
                }
            }
        }
    }
};
