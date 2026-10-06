class Solution {
    public boolean isPalindrome(String s) {
        String lowerCase = s.toLowerCase();

        int left = 0, right = s.length() - 1;
        while (left <= right) {
            if (!('a' <= lowerCase.charAt(left) && lowerCase.charAt(left) <= 'z' || '0' <= lowerCase.charAt(left) && lowerCase.charAt(left) <= '9')) {
                left++;
                continue;
            }
            if (!('a' <= lowerCase.charAt(right) && lowerCase.charAt(right) <= 'z' || '0' <= lowerCase.charAt(right) && lowerCase.charAt(right) <= '9')) {
                right--;
                continue;
            }

            if (lowerCase.charAt(left) != lowerCase.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
}
