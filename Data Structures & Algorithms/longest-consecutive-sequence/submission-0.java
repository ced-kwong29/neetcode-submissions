class Solution {
    public int longestConsecutive(int[] nums) {
        Map<Integer, Integer> graph = new HashMap<>();

        int maxSequence = 0;
        for (int n : nums) {
            if (!graph.containsKey(n)) {
                graph.put(n, graph.getOrDefault(n - 1, 0) + graph.getOrDefault(n + 1, 0) + 1);
                graph.put(n - graph.getOrDefault(n - 1, 0), graph.get(n));
                graph.put(n + graph.getOrDefault(n + 1, 0), graph.get(n));
                maxSequence = Math.max(maxSequence, graph.get(n));
            }
        }

        return maxSequence;
    }
}
