class Solution {

  public int findLeastNumOfUniqueInts(int[] arr, int k) {
    int i;

    // count occurrences
    Map<Integer, Integer> freq = new HashMap<>();
    for (i = 0; i < arr.length; i++) {
      freq.put(arr[i], freq.getOrDefault(arr[i], 0) + 1);
    }
    // make p-queue
    PriorityQueue<Map.Entry<Integer, Integer>> pQ = new PriorityQueue<>(
        (e1, e2) ->
      e1.getValue() - e2.getValue()
    );
    pQ.addAll(freq.entrySet());

    Map.Entry<Integer, Integer> e;
    int v;

    // remove as many low-frequency items as possible
    while (k > 0 && !pQ.isEmpty()) {
      e = pQ.peek();
      v = e.getValue();
      if (v <= k) {
        k -= v;
        pQ.poll();
      } else {
        break;
      }
    }

    return pQ.size();
  }
}
