/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {

    private ListNode addDigit(int carry, ListNode l1, ListNode l2) {
        if (l1 == null && l2 == null && carry == 0) {
            return null;
        }

        ListNode pos = new ListNode();

        int digit = carry;
        if (l1 != null) {
            digit += l1.val;
            l1 = l1.next;
        }
        if (l2 != null) {
            digit += l2.val;
            l2 = l2.next;
        }

        if (digit > 9) {
            carry = 1;
            pos.val = digit % 10;
        } else {
            carry = 0;
            pos.val = digit;
        }

        pos.next = addDigit(carry, l1, l2);
        return pos;
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return addDigit(0, l1, l2);
    }
}
