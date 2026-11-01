class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = 1, 1

        end = len(nums)
        product = [1] * end
        for i in range(end):
            product[i] *= prefix
            product[end - 1 - i] *= suffix

            prefix *= nums[i]
            suffix *= nums[end - 1 - i]
        
        return product