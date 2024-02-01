public class Tuple {

  public final int idx;
  public final int val;

  public Tuple(int idx, int val) {
    this.idx = idx;
    this.val = val;
  }
}

class Solution {

  public int[] dailyTemperatures(int[] temperatures) {
    Stack<Tuple> stack = new Stack<Tuple>();
    int[] res = new int[temperatures.length];
    int curr;
    Tuple top;

    for (int i = 1; i < temperatures.length; i++) {
      top = new Tuple(i - 1, temperatures[i - 1]);
      stack.add(top);
      curr = temperatures[i];
      while (!stack.empty() && curr > stack.peek().val) {
        top = stack.pop();
        res[top.idx] = i - top.idx;
      }
    }
    return res;
  }
}
