class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> parentheses = Map.of(')', '(',
                                                        ']', '[',
                                                        '}', '{');
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (!parentheses.containsKey(c)) {
                stack.push(c);
                continue;
            }

            if (!stack.isEmpty() && parentheses.get(c) == stack.peek()) {
                stack.pop();
            } else {
                return false;
            }
        }

        return stack.isEmpty();
    }
}
