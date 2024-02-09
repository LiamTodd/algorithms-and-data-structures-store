class Solution {

  public int jump(int[] nums) {
    // early exit
    if (nums.length < 2) {
      return 0;
    }

    // DP approach
    // memo stores the minimum number of jumps to get to that index
    int l = nums.length;
    int[] memo = new int[l];
    int i;
    int j;
    int min;
    // pre-process memo: all elements are unreached except element 0
    memo[0] = 0;
    for (i = 1; i < l; i++) {
      memo[i] = -1;
    }

    for (i = 1; i < l; i++) {
      min = l;
      for (j = 0; j < i; j++) {
        // if j can be reached, would improve the minimum, i can be reached from j,
        if (memo[j] >= 0 && memo[j] < min && nums[j] >= i - j) {
          min = memo[j];
        }
      }
      memo[i] = min + 1;
    }

    return memo[l - 1];
  }
}
