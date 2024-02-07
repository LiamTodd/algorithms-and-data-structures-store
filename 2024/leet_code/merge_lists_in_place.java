class Solution {

  // fully optimised solution - no local variables used and O(m+n) complexity
  public void merge(int[] nums1, int m, int[] nums2, int n) {
    while (m > 0 && n > 0) {
      // put the larger of nums1[j] and nums2[k] into nums1[i], decrement pointers
      if (nums1[m - 1] > nums2[n - 1]) {
        nums1[m + n - 1] = nums1[m - 1];
        m--;
      } else {
        nums1[m + n - 1] = nums2[n - 1];
        n--;
      }
    }
    // put remaining elements of nums2 into nums1
    while (n > 0) {
      nums1[n - 1] = nums2[n - 1];
      n--;
    }
  }
}
// This is more readable, but less optimised towards memory
// class Solution {
//     public void merge(int[] nums1, int m, int[] nums2, int n) {
//         // point to last index (the one being filled)
//         int i = m + n - 1;
//         int j = m - 1;
//         int k = n - 1;
//         while (j >= 0 && k >= 0){
//             // put the larger of nums1[j] and nums2[k] into nums1[i], decrement pointers
//             if (nums1[j] > nums2[k]){
//                 nums1[i] = nums1[j];
//                 j--;
//             }
//             else{
//                 nums1[i] = nums2[k];
//                 k--;
//             }
//             // always decrement i, because one more element in nums1 is sorted
//             i--;
//         }
//         // put remaining elements of nums2 into nums1
//         while (k >= 0 && i >= 0){
//             nums1[i] = nums2[k];
//             i --;
//             k --;
//         }
//     }
// }
