class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        nums.sort()
        
        end = len(nums)
        for i in range(end):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left, right = i + 1, end - 1
            while left < right:
                tripletSum = nums[i] + nums[left] + nums[right]
                if tripletSum < 0:
                    left += 1
                elif tripletSum > 0:
                    right -= 1
                else :
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    # right -= 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1

        return triplets