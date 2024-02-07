class Solution {

  public int majorityElement(int[] nums) {
    // only works if the majority element occurs more than half the time
    int candidate = nums[0];
    int votes = 1;
    int i;
    for (i = 1; i < nums.length; i++) {
      if (nums[i] == candidate) {
        votes++;
      } else {
        votes--;
      }
      if (votes == 0) {
        candidate = nums[i];
        votes = 1;
      }
    }
    return candidate;
  }
}
