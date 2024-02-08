class Solution {

  public boolean isPalindromeEfficient(String s) {
    // this solution avoids modifying the string

    if (s.length() < 2) {
      return true;
    }
    int l = 0;
    int r = s.length() - 1;
    while (l < r) {
      if (!Character.isLetterOrDigit(s.charAt(l))) {
        l++;
        continue;
      }
      if (!Character.isLetterOrDigit(s.charAt(r))) {
        r--;
        continue;
      }
      if (
        Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))
      ) {
        return false;
      }
      l++;
      r--;
    }
    return true;
  }

  public boolean isPalindrome(String s) {
    // early exit
    if (s.length() < 2) {
      return true;
    }
    // Remove non alpha-numeric characters and convert to lowercase
    s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();

    // check mirror-chars
    int l = 0;
    int r = s.length() - 1;
    while (l < r) {
      if (s.charAt(l) != s.charAt(r)) {
        return false;
      }
      l++;
      r--;
    }
    return true;
  }
}
