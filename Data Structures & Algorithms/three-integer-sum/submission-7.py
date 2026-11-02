class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        end = len(nums)

        nums.sort()
        for i in range(end):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left, right = i + 1, end - 1
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                if currSum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1

                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                        
                elif currSum < 0:
                    left += 1
                else:
                    right -= 1

        return triplets