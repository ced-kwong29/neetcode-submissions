class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack();

        for (String t : tokens) {
            if (t.equals("+")) {
                stack.push(stack.pop() + stack.pop());
            } else if (t.equals("-")) {
                stack.push(-stack.pop() + stack.pop());
            } else if (t.equals("*")) {
                stack.push(stack.pop() * stack.pop());
            } else if (t.equals("/")) {
                int num = stack.pop();
                stack.push(stack.pop() / num);
            } else {
                stack.push(Integer.valueOf(t));
            }
            System.out.println(stack);
        }

        return stack.peek();
    }
}
