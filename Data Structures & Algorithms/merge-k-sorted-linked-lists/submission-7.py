# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def sort(list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1

            dummy = ListNode()
            pos = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    pos.next = list1
                    list1 = list1.next
                else:
                    pos.next = list2
                    list2 =  list2.next

                pos = pos.next
        
            if not list1:
                pos.next = list2
            if not list2:
                pos.next = list1
            return dummy.next
        
        
        if not lists:
            return None

        total = len(lists)
        if total == 1:
            return lists[0]

        mergedLists = []
        start = 0
        if total % 2 > 0:
            mergedLists.append(lists[0])
            start = 1

        for i in range(start, len(lists), 2):
            mergedLists.append(sort(lists[i], lists[i + 1]))

        return self.mergeKLists(mergedLists)