class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> allPerms = new ArrayList<>(); 

        if (nums.length == 1) {
            List<Integer> singleItem = new ArrayList<>();
            singleItem.add(nums[0]);
            allPerms.add(singleItem);
        } else {
            for (int i = 0; i < nums.length; i++) {
                int num = nums[i];

                int[] remaining = new int[nums.length - 1];
                int ndx = 0;
                for (int j = 0; j < nums.length; j++) {
                    if (j != i) {
                        remaining[ndx++] = nums[j];
                    }
                }

                for (List<Integer> perm : permute(remaining)) {
                    perm.add(num);
                    allPerms.add(new ArrayList<>(perm));
                }
            }
        }

        return allPerms;
    }
}
