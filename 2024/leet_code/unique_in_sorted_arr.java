class Solution {

  // In-place counting of unique elements in a sorted array

  public int removeDuplicates(int[] nums) {
    int curr = 0;
    int cand = 1;
    while (cand < nums.length) {
      if (nums[curr] == nums[cand]) {
        cand++;
      } else {
        nums[curr + 1] = nums[cand];
        curr++;
      }
    }
    return curr + 1;
  }
}
