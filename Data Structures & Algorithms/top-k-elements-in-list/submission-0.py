class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        op_dict= {}
        for i in nums:
            if i in op_dict:
                op_dict[i]=op_dict[i]+1
            else:
                op_dict[i]=1
        sorted_key = sorted(op_dict.items(),key = lambda x:x[1],reverse=True)
        result = [x[0] for x in sorted_key[:k]]
        return result