// Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

class Solution {

  public int[] countBits(int n) {
    int[] res = new int[n + 1];
    int curr;
    for (int i = 0; i <= n; i++) {
      curr = i;
      while (curr > 0) {
        if (curr % 2 == 1) {
          res[i]++;
        }
        curr = curr / 2;
      }
    }
    return res;
  }
}
