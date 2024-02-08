class Solution {

  public int strStr(String haystack, String needle) {
    int i = 0; // haystack pointer
    int j = 0; // needle pointer
    int h = haystack.length();
    int n = needle.length();
    while (i < h && j < n) {
      if (haystack.charAt(i) == needle.charAt(j)) {
        j++;
        if (j == n) {
          return i - j + 1;
        }
      } else {
        // walk back haystack pointer only as far as needed
        i = i - j;
        // reset needle pointer
        j = 0;
      }
      // always walk forwards in haystack
      i++;
    }
    return -1;
  }
}
