# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head

        # Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Put second half into stack
        stack = []
        curr = slow.next
        slow.next = None

        while curr:
            stack.append(curr)
            curr = curr.next

        # Interleave first half and reversed second half
        curr = head

        while stack:
            node = stack.pop()

            temp = curr.next
            curr.next = node
            node.next = temp

            curr = temp