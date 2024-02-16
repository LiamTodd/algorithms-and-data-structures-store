class Solution {

  public boolean canConstruct(String ransomNote, String magazine) {
    // this is solved as a substring matching problem with the extra step of sorting the strings

    char[] sortedRansomNote = ransomNote.toCharArray();
    Arrays.sort(sortedRansomNote);
    char[] sortedMagazine = magazine.toCharArray();
    Arrays.sort(sortedMagazine);

    int i; // magazine pointer
    int j = 0; // ransom note pointer
    for (i = 0; i < magazine.length(); i++) {
      // always walk forwards in magazine, only walk forwards in ransom note if match found
      if (sortedMagazine[i] == sortedRansomNote[j]) {
        j++;
        // early exit: ransom note can be constructed
        if (j == ransomNote.length()) {
          return true;
        }
      }
    }
    return false;
  }
}
