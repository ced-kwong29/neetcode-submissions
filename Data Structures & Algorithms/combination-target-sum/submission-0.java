class Solution {
    private List<List<Integer>> allCombos = new ArrayList<>();

    private void generateCombo(int[] nums, int target, int index, List<Integer> combo) {
        if (target == 0) {
            allCombos.add(combo);
            return;
        }

        for (int i = index; i < nums.length; i++) {
            if (target - nums[i] >= 0) {
                List<Integer> updatedCombo = new ArrayList<>(combo);
                updatedCombo.add(nums[i]);
                generateCombo(nums, target - nums[i], i, updatedCombo);
            }
        }
    }

    public List<List<Integer>> combinationSum(int[] nums, int target) {
        generateCombo(nums, target, 0, new ArrayList<>());
        return allCombos;
    }
}
