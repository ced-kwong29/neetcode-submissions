class Solution {
    public boolean hasDuplicate(int[] nums) {
        List<Integer> seen = new ArrayList<>();
        for (int n : nums) {
            if (seen.contains(n)) {
                return true;
            }
            seen.add(n);
        }
        return false;
    }
}
