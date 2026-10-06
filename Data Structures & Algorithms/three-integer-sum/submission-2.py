class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        nums.sort()

        end = len(nums)
        for i in range(end):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left = i + 1
            right = end - 1
            while left < right:
                threeSum = nums[i] + nums[right] + nums[left]
                if threeSum == 0:
                    triplets.append([nums[i], nums[right], nums[left]])

                    left += 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1

                elif threeSum < 0:
                    left += 1
                else:
                    right -= 1
            
        return triplets