class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        count=1
        max_count= 0
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]+1:
                count +=1
            elif nums[i+1]==nums[i] or i == len(nums)-1:
                continue
            else:
                max_count = max(count, max_count)
                count = 1    
        max_count = max(count,max_count)
        return max_count


        



        