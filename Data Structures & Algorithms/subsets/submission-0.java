class Solution {
    private List<List<Integer>> allSubsets = new ArrayList<>();

    private void generateSubset(int[] nums, int index, List<Integer> subset) {
        allSubsets.add(new ArrayList<>(subset));

        if (index == nums.length) {
            return;
        }

        for (int i = index; i < nums.length; i++) {
            subset.add(nums[i]);
            generateSubset(nums, i + 1, subset);
            subset.remove(subset.size() - 1);
        }
    }

    public List<List<Integer>> subsets(int[] nums) {
        generateSubset(nums, 0, new ArrayList<>());
        return allSubsets;
    }
}
