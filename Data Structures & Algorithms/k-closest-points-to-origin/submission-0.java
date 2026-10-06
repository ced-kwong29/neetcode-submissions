class Solution {
    public int[][] kClosest(int[][] points, int k) {
        Map<int[], Integer> distance = new HashMap<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> distance.get(b) - distance.get(a));

        for (int[] p : points) {
            distance.put(p, p[0]*p[0] + p[1]*p[1]);
            pq.add(p);
            if (pq.size() > k) {
                pq.poll();
            }
        }

        return pq.toArray(new int[k][]);
    }
}
