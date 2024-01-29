// Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

// Implement the MyQueue class:

// void push(int x) Pushes element x to the back of the queue.
// int pop() Removes the element from the front of the queue and returns it.
// int peek() Returns the element at the front of the queue.
// boolean empty() Returns true if the queue is empty, false otherwise.
// Notes:

// You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
// Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

class MyQueue {

  private Stack<Integer> readStack;
  private Stack<Integer> writeStack;

  public MyQueue() {
    this.writeStack = new Stack<Integer>();
    this.readStack = new Stack<Integer>();
  }

  public void push(int x) {
    this.writeStack.push(x);
  }

  public int pop() {
    while (this.writeStack.size() > 0) {
      this.readStack.push(this.writeStack.pop());
    }
    int res = this.readStack.pop();
    while (this.readStack.size() > 0) {
      this.writeStack.push(this.readStack.pop());
    }
    return res;
  }

  public int peek() {
    while (this.writeStack.size() > 0) {
      this.readStack.push(this.writeStack.pop());
    }
    int res = this.readStack.peek();
    while (this.readStack.size() > 0) {
      this.writeStack.push(this.readStack.pop());
    }
    return res;
  }

  public boolean empty() {
    return this.writeStack.size() == 0;
  }
}
/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
