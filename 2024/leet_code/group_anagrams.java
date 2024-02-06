class Solution {

  public List<List<String>> groupAnagrams(String[] strs) {
    char[] chars;
    String key;
    List<List<String>> res = new ArrayList<>();
    Map<String, List<String>> t = new HashMap<>();

    for (String s : strs) {
      chars = s.toCharArray();
      Arrays.sort(chars);
      key = new String(chars);

      if (t.get(key) != null) {
        t.get(key).add(s);
      } else {
        List<String> l = new ArrayList<>();
        l.add(s);
        t.put(key, l);
      }
    }

    for (String k : t.keySet()) {
      res.add(t.get(k));
    }

    return res;
  }
}
