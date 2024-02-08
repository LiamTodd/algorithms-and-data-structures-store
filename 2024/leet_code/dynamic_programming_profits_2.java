class Solution {

  public int maxProfit(int[] prices) {
    // dynamic programming approach with overlapping subproblems
    // max profit on i'th day is max(profit[prev] + max(prices[i] - prices[prev]), 0) for all previous days, prev
    int[] memo = new int[prices.length]; // all initialise to 0
    int i;
    int j;
    int max;
    for (i = 1; i < prices.length; i++) {
      max = 0;
      for (j = 0; j < i; j++) {
        if (memo[j] + Math.max(prices[i] - prices[j], 0) > max) {
          max = memo[j] + Math.max(prices[i] - prices[j], 0);
        }
      }
      memo[i] = max;
    }
    return memo[prices.length - 1];
  }
}
