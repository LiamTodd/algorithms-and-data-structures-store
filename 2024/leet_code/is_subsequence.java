class Solution {

  public boolean isSubsequence(String s, String t) {
    int i = 0;
    int j = 0;
    int l = s.length();
    while (i < l && j < t.length()) {
      if (s.charAt(i) == t.charAt(j)) {
        i++;
      }
      j++;
    }
    return i == l;
  }
}
