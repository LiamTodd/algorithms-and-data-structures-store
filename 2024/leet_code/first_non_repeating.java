class Solution {

  public int firstUniqChar(String s) {
    // originally used hashmap, but went for array since we know the range of elements, and get guaranteed O(1) access
    int[] charCount = new int[26];
    int i;
    int l = s.length();
    for (i = 0; i < l; i++) {
      // index = ascii value - 97, because ascii (a) = 97
      charCount[(int) s.charAt(i) - 97]++;
    }
    for (i = 0; i < l; i++) {
      if (charCount[(int) s.charAt(i) - 97] == 1) {
        return i;
      }
    }
    return -1;
  }
}
