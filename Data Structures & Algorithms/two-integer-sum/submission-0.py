class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dif_map = {} 
        for i,num in enumerate(nums):
            diff = target - num
            if num in dif_map:
                return [dif_map[num],i]
            else:
                dif_map[diff]=i


        