class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int n : nums) {
            freq.put(n, freq.getOrDefault(n, 0) + 1);
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> freq.get(b) - freq.get(a));
        for (int n : freq.keySet()) {
            pq.add(n);
        }

        int[] topK = new int[k];
        int size = 0;
        while (!pq.isEmpty() && size < k) {
            topK[size] = pq.poll();
            size++;
        }

        return topK;
    }
}
