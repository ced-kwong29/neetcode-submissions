class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        for (int n : stones) {
            pq.add(n);
        }

        int count = stones.length;
        while (count > 1) {
            int diff = Math.abs(pq.poll() - pq.poll());
            if (diff == 0) {
                count -= 2;
                continue;
            }
            pq.add(diff);
            count--;
        }
        return pq.isEmpty() ? 0 : pq.poll();
    }
}
