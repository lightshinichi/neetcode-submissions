class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        
        std::set<int> soln;
        for (int i = 0;i<nums.size();i++){
             if (soln.count(nums[i])> 0) {
                 return true;     
    } 
    
    soln.insert(nums[i]);
            
            
            
        }
        return false;
    }
};

