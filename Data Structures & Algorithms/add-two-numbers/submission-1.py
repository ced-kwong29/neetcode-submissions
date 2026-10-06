# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 and l2:
            nodeSum = l1.val + l2.val + carry

            if nodeSum >= 10:
                nodeSum -= 10
                carry = 1
            else:
                carry = 0

            curr.next = ListNode(val=nodeSum)
            curr = curr.next

            l1, l2 = l1.next, l2.next

        while l1:
            nodeSum = l1.val + carry
            if nodeSum >= 10:
                nodeSum -= 10
                carry = 1
            else:
                carry = 0
            
            curr.next = ListNode(val=nodeSum)
            curr = curr.next

            l1 = l1.next

        while l2:
            nodeSum = l2.val + carry
            if nodeSum >= 10:
                nodeSum -= 10
                carry = 1
            else:
                carry = 0
            
            curr.next = ListNode(val=nodeSum)
            curr = curr.next

            l2 = l2.next
        
        if carry > 0:
            curr.next = ListNode(val = carry)

        return dummy.next