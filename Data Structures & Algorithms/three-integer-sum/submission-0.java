class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> triplets = new ArrayList<>();

        Arrays.sort(nums);
        int end = nums.length;
        for (int i = 0; i < end; i++) {
            if (i > 0 && nums[i - 1] == nums[i]) {
                continue;
            }

            int j = i + 1, k = end - 1;
            while (j < k) {
                int tripletSum = nums[i] + nums[j] + nums[k];
                if (tripletSum > 0) {
                    k--;
                } else if (tripletSum < 0) {
                    j++;
                } else {
                    triplets.add(List.of(nums[i], nums[j], nums[k]));
                    do {
                        j++;
                    } while (j < k && nums[j - 1] == nums[j]);
                }
            }
        }

        return triplets;
    }
}
