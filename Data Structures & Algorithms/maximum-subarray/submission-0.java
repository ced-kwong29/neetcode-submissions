class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = Integer.MIN_VALUE, currSum = 0;
        for (int n : nums) {
            if (currSum < 0) {
                currSum = 0;
            }

            currSum += n;
            if (maxSum < currSum) {
                maxSum = currSum;
            }
        }

        return maxSum;
    }
}
