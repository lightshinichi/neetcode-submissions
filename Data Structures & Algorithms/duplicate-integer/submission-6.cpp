class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> duplicate;
        
        for(auto i= nums.begin(); i != nums.end();i++){
            if (duplicate.contains(*i)){
                return true;
            }
            else{
                duplicate.insert(*i);
            }
        }
        return false;
    }
        };