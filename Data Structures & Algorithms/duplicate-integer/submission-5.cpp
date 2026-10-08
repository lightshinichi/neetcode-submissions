class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        if (nums.size() ==0){
            return false;
        }
        std::sort(nums.begin(),nums.end());
        
        for (auto i = nums.begin(); i!= nums.end()-1;i++){
            if (*i == *std::next(i)){
                return true;
            }

        }

        return false;
    }
};