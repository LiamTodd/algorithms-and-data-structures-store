/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {

  public boolean hasCycle(ListNode head) {
    // tortiose and hare algorithm
    ListNode fast = head;
    while (fast != null && fast.next != null) {
      head = head.next;
      fast = fast.next.next;
      if (head == fast) {
        return true;
      }
    }
    return false;
  }
  // public boolean hasCycle(ListNode head) {
  //     ArrayList<ListNode> list = new ArrayList<ListNode>();
  //     while(head != null){
  //         if (list.contains(head)){
  //             return true;
  //         }
  //         list.add(head);
  //         head = head.next;
  //     }
  //     return false;
  // }
}
