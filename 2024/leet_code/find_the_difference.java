class Solution {

  public char findTheDifference(String s, String t) {
    // same as ascii diff, in one line
    return (char) (t.chars().sum() - s.chars().sum());
  }

  public char findTheDifferenceAsciiDiff(String s, String t) {
    // sum of ascii values of s and t
    int sumS = s.chars().sum();
    int sumT = t.chars().sum();

    // difference of ascii values
    int diff = sumT - sumS;

    // convert diff to ascii value
    return (char) diff;
  }

  public char findTheDifferencePQueue(String s, String t) {
    // sort characters of s and t using p-queues
    PriorityQueue<Character> sPQ = new PriorityQueue<Character>();
    PriorityQueue<Character> tPQ = new PriorityQueue<Character>();
    for (int i = 0; i < t.length(); i++) {
      if (i < s.length()) {
        sPQ.add(s.charAt(i));
      }
      tPQ.add(t.charAt(i));
    }

    // pop elements and compare
    char sE;
    char tE;
    while (!sPQ.isEmpty()) {
      sE = sPQ.remove();
      tE = tPQ.remove();
      if (sE != tE) {
        return tE;
      }
    }
    // last element of tPQ must be the added element
    return tPQ.remove();
  }
}
