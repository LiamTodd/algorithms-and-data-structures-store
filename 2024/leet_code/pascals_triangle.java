class Solution {

  public List<List<Integer>> generate(int numRows) {
    List<List<Integer>> res = new ArrayList<List<Integer>>();
    res.add(new ArrayList<Integer>());
    res.get(0).add(1);

    int sumAbove;
    for (int i = 1; i < numRows; i++) {
      res.add(new ArrayList<Integer>());
      for (int j = 0; j < i + 1; j++) {
        if (j == 0 || j == i) {
          // first and last element of each row is the sum of the first/last (same number) in the previous row
          res.get(i).add(res.get(i - 1).get(0));
        } else {
          // all other elements equal the sum of the two elements directly above it
          res.get(i).add(res.get(i - 1).get(j - 1) + res.get(i - 1).get(j));
        }
      }
    }
    return res;
  }
}
