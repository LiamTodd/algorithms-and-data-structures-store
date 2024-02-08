class Solution {

  private static void reverse(int[] nums, int start, int end) {
    int temp;
    while (start < end) {
      temp = nums[start];
      nums[start] = nums[end];
      nums[end] = temp;
      start++;
      end--;
    }
  }

  public void rotate(int[] nums, int k) {
    // [1 2 3 4 5 6 7 8] k = 12

    // reverse
    // [8 7 6 5 4 3 2 1]

    // normalise k
    // k = k % length = 4

    // reverse left and right of k, independently
    // [5 6 7 8 | 1 2 3 4]

    // reverse array
    Solution.reverse(nums, 0, nums.length - 1);

    // reverse on either side of normalised k
    k = k % nums.length;
    Solution.reverse(nums, 0, k - 1);
    Solution.reverse(nums, k, nums.length - 1);
  }
}
