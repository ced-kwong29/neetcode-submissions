# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        slow = slow.next
        stack = []
        while slow:
            stack.append(slow)
            print(slow.val)
            slow = slow.next

        currNode = head
        while len(stack) > 1:
            nextNode = currNode.next

            currNode.next = stack.pop()
            currNode.next.next = nextNode

            currNode = nextNode
        
        stack[-1].next = None