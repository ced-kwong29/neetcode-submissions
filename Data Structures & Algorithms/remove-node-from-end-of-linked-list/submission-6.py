# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        remaining = 0
        pos = head
        while pos:
            remaining += 1
            pos = pos.next

        prev, pos = dummy, head
        while remaining > n:
            prev = pos
            pos = pos.next
            remaining -= 1

        prev.next = pos.next
        return dummy.next