class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<int, string> dict_s;
        unordered_map<int, string> dict_t;

        for(int i=0;i<s.size();i++){ // fill in s dict
            dict_s[s[i]] += s[i];
            // cout << "/n";
            // cout << dict_s[s[i]];
        }
        for(int i=0;i<t.size();i++){ // fill in t dict
            dict_t[t[i]] += t[i];
            // cout << "/n";
            // cout << dict_t[t[i]];
        }
        // compare s dict and t dict
        if(dict_t == dict_s){
            return true;
        }
        return false;
    }
};
