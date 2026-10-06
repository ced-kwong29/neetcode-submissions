class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;

        int boughtFor = prices[0];
        for (int i = 1; i < prices.length; i++) {
            if (boughtFor > prices[i]) {
                boughtFor = prices[i];
            }

            int currProfit = prices[i] - boughtFor;
            if (maxProfit < currProfit) {
                maxProfit = currProfit;
            }
        }

        return maxProfit;
    }
}
