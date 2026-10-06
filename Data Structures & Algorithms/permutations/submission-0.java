class Solution {
    private List<List<Integer>> allPerms = new ArrayList<>();

    private void generatePerm(int[] nums, List<Integer> perm) {
        if (perm.size() == nums.length) {
            allPerms.add(perm);
            return;
        }

        for (int n : nums) {
            if (!perm.contains(n)) {
                List<Integer> updatedPerm = new ArrayList<>(perm);
                updatedPerm.add(n);
                generatePerm(nums, updatedPerm);
            }
        }
    }

    public List<List<Integer>> permute(int[] nums) {
        generatePerm(nums, new ArrayList<>());
        return allPerms;
    }
}
