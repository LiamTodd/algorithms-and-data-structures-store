class Solution {

  public String frequencySort(String s) {
    // count occurrences of chars in hash table: O(n)
    HashMap<Character, Integer> t = new HashMap<>();
    for (char c : s.toCharArray()) {
      if (t.get(c) == null) {
        t.put(c, 1);
      } else {
        t.put(c, t.get(c) + 1);
      }
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
    char[] sorted = new char[s.length()];
    int i = 0;
    int j;
    Map.Entry<Character, Integer> e;
    while (!pq.isEmpty()) {
      e = pq.peek();
      for (j = 0; j < e.getValue(); j++) {
        sorted[i] = e.getKey();
        i++;
      }
      pq.poll();
    }

    return new String(sorted);
  }
}
