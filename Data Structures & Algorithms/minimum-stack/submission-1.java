class MinStack {
    private Stack<Integer> orderedStack, minStack;

    public MinStack() {
        orderedStack = new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int val) {
        orderedStack.push(val);
        minStack.push(minStack.isEmpty() ? val : Math.min(val, minStack.peek()));
    }
    
    public void pop() {
        orderedStack.pop();
        minStack.pop();
    }
    
    public int top() {
        return orderedStack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
