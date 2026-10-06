class Solution {
    List<List<Integer>> allCombos = new ArrayList<>();

    private void generateCombo(int[] candidates, int index, int target, List<Integer> combo) {
        if (target == 0) {
            allCombos.add(new ArrayList<>(combo));
            return;
        }

        int end = combo.size();
        for (int i = index; i < candidates.length; i++) {
            if (i > index && candidates[i - 1] == candidates[i]) {
                continue;
            }
            int diff = target - candidates[i];
            if (diff >= 0) {
                combo.add(candidates[i]);
                generateCombo(candidates, i + 1, diff, combo);
                combo.remove(end);
            }
        }
    }

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        generateCombo(candidates, 0, target, new ArrayList<>());
        return allCombos;
    }
}
