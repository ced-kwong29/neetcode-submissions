class Solution {
    private List<List<Integer>> allSubsets = new ArrayList<>();

    private void generateSubset(int index, int[] nums, List<Integer> subset) {
        allSubsets.add(new ArrayList<>(subset));

        int end = subset.size();
        for (int i = index; i < nums.length; i++) {
            if (i > index && nums[i - 1] == nums[i]) {
                continue;
            }
            subset.add(nums[i]);
            generateSubset(i + 1, nums, subset);
            subset.remove(end);
        }
    }

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        generateSubset(0, nums, new ArrayList<>());
        return allSubsets;
    }
}
