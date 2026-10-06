class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> freq = new HashMap<>();
        int count = 0;
        for (char c : s.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
            count++;
        }

        for (char c : t.toCharArray()) {
            int remaining = freq.getOrDefault(c, 0);
            if (remaining == 0) {
                return false;
            }
            freq.put(c, remaining - 1);
            count--;
        }
        return count == 0;
    }
}
