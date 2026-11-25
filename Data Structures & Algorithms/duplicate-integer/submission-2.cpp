class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
    unordered_map<int, string> dict;
    int i = 0;

    for (i=0;i<nums.size();i++) { // iterate through list
        // if nums[i] in dict, return false. else, add nums[i] to dict
        cout << to_string(nums[i]);
        if (dict[nums[i]] == "1") {
            return true;
        }
        else {
            dict[nums[i]] = "1";
        }
    }
    return false;
    }
};