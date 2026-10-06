class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0;

        Map<Character, Boolean> seen = new HashMap<>();

        int left = 0, right = 0, end = s.length();

        while (right < end) {
            char c = s.charAt(right);
            if (seen.containsKey(c) && seen.get(c)) {
                if (maxLength < right - left) {
                    maxLength = right - left;
                }
                seen.put(s.charAt(left++), false);
                continue;
            }
            seen.put(c, true);
            right++;
        }

        return Math.max(maxLength, right - left);
    }
}
