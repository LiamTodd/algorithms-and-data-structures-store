class Solution {

  public boolean canJump(int[] nums) {
    // 'recharging walk' idea
    // walk as long as there is enough charge
    // at each index, refuel or decrement, whatever gives the most charge
    int charge = 1;
    int i = 0;
    int l = nums.length;
    while (i < l && charge > 0) {
      // charge is the greater of the current charge decremented, or the new amount of charge
      charge = Math.max(nums[i], charge - 1);
      i++;
    }
    return i == l;
  }

  public boolean canJumpDynamicProgramming(int[] nums) {
    // early exit
    if (nums.length < 2) {
      return true;
    }

    // DP approach
    // memo stores whether you can, or cannot reach the current index
    int l = nums.length;
    int i;
    int jump;
    boolean[] memo = new boolean[l];
    // we start at 0, so memo[0] is always true
    memo[0] = true;

    for (i = 0; i < l; i++) {
      // start jumping from this index only if we could have got there from a previous index
      if (memo[i]) {
        jump = 1;
        // jump from the index, as long as the jump is valid
        while (jump <= nums[i] && i + jump < l) {
          // exit early: we have reached the end of the array
          if (i + jump == l - 1) {
            return true;
          }
          memo[i + jump] = true;
          jump++;
        }
      }
    }

    return false;
  }
}
