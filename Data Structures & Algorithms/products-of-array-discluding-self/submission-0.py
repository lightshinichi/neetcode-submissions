class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            # print(i)
            product = 1
            for j in range(len(nums)):
                # print(j)
                if i != j:
                    product *= nums[j]
            # print(product)
            output.append(product)
        return output
