
// implement stack using queue: can be done using one queue!! Smart
public class MyStack {

    /** Initialize your data structure here. */
    public MyStack() {
        
    }
    
    private Queue<Integer> q1 = new LinkedList<>();
    
    /** Push element x onto stack. */
    public void push(int x) {
        q1.add(x);
        int len = q1.size();
        while ( len > 1) {
            q1.add(q1.remove());
            len --;
        }
        
        
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        
        return q1.remove();
        
    }
    
    /** Get the top element. */
    public int top() {
        
        // int tmp = 0;
        // tmp = q1.remove();
        // q1.add(tmp);
        
        // return tmp;
        return q1.peek();
        
    }
    
    /** Returns whether the stack is empty. */
    public boolean empty() {
        
        return q1.isEmpty();
        
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
