class Solution {

  public int missingNumber(int[] nums) {
    // no need to sort
    int[] range = new int[nums.length + 1];
    int i;
    for (i = 0; i < nums.length; i++) {
      range[nums[i]] = 1;
    }
    for (i = 0; i <= range.length; i++) {
      if (range[i] == 0) {
        break;
      }
    }
    return i;
  }
}
