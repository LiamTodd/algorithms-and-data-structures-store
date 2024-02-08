class Solution {

  public int numSquares(int n) {
    // overlapping subproblem: DP[v] = the minimum number of squares which can be used to make value=v
    // DP[v] = 0 if v = 0
    // DP[v] = 1 + min(DP[v-square]) for square in squares
    int[] memo = new int[n + 1]; // all elements initialised to 0
    int i = 0;
    int j;
    int min;
    for (i = 1; i < n + 1; i++) {
      min = i;
      for (j = 1; j * j <= i; j++) {
        if (memo[i - j * j] < min) {
          min = memo[i - j * j];
        }
      }
      memo[i] = 1 + min;
    }
    return memo[n];
  }
}
