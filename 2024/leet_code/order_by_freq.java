class Solution {

  // beats 88%

  public String frequencySort(String s) {
    // count occurrences of chars in hash table: O(n)
    HashMap<Character, Integer> t = new HashMap<>();
    int i;
    int l = s.length();
    char c;
    for (i = 0; i < l; i++) {
      c = s.charAt(i);
      t.compute(c, (key, value) -> (value == null) ? 1 : value + 1);
    }

    // put hashtable entries into priority queue, prioritised on count: O(nlog(n))
    PriorityQueue<Map.Entry<Character, Integer>> pq = new PriorityQueue<>(
        (e1, e2) ->
      e2.getValue() - e1.getValue()
    );
    for (Map.Entry<Character, Integer> e : t.entrySet()) {
      pq.add(e);
    }

    // pop from queue to create new string: O(nlog(n))
    char[] sorted = new char[l];
    int j;
    int k;
    Map.Entry<Character, Integer> e;
    i = 0;
    while (!pq.isEmpty()) {
      e = pq.poll();
      c = e.getKey();
      k = e.getValue();
      for (j = 0; j < k; j++) {
        sorted[i] = c;
        i++;
      }
    }

    return new String(sorted);
  }
}
