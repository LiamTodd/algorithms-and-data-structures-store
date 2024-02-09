class Solution {

  public int lengthOfLastWord(String s) {
    // Example 1:
    // Input: s = "Hello World"
    // Output: 5
    // Explanation: The last word is "World" with length 5.
    // Example 2:
    // Input: s = "   fly me   to   the moon  "
    // Output: 4
    // Explanation: The last word is "moon" with length 4.

    int l = s.length();
    int i = l - 1;
    int rightPadding;

    // preprocess - walk past spaces at the end of the string
    while (s.charAt(i) == ' ') {
      i--;
    }
    rightPadding = l - i - 1;

    // walk until a space is found
    for (i = l - rightPadding - 1; i >= 0; i--) {
      if (s.charAt(i) == ' ') {
        break;
      }
    }

    // calculate the length
    return l - i - rightPadding - 1;
  }
}
