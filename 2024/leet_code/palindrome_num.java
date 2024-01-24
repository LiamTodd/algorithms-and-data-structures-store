class Solution {

  public boolean isPalindrome(int x) {
    // special case: 0 is palindrome, will break num_digits calculation
    if (x == 0) {
      return true;
    }
    // special case: negative cannot be palindrome
    if (x < 0) {
      return false;
    }

    int num_digits = (int) Math.floor(Math.log10(Math.abs(x)) + 1);

    // early exit: length 1 = palindrome
    if (num_digits == 1) {
      return true;
    }

    int[] digits = new int[num_digits];
    int i = 0;
    while (x > 0) {
      digits[i] = x % 10;
      x = x / 10;
      i++;
    }
    for (int l = 0; l < num_digits / 2; l++) {
      int r = num_digits - l - 1;
      if (digits[l] != digits[r]) {
        return false;
      }
    }
    return true;
  }
}
