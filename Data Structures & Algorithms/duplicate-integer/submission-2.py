class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Optimized soln
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False

        #Alternate soln
        # if len(nums)==0:
        #     return False
        # nums = sorted(nums)
        # last_num= nums[0]
        # for num in nums[1:]:
        #     if num==last_num:
        #         return True
        #     else:
        #         last_num=num
        # return False
        

            
             

        