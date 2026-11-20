# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not (head and head.next):
            return

        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        stack = []
        pos = slow.next
        slow.next = None

        while pos:
            stack.append(pos)
            pos = pos.next

        pos = head
        while stack:
            tmp = pos.next

            node = stack.pop()
            pos.next = node
            node.next = tmp

            pos = tmp
            
            
        