# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1, list2):
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
                    list2 = list2.next

                pos = pos.next


            pos.next = list2 if not list1 else list1
            return dummy.next

        if not lists:
            return None

        total = len(lists)
        if total == 1:
            return lists[0]

        isEven = total % 2 == 0
        mergedLists = [] if isEven else [lists[total - 1]]
        for i in range(0 if isEven else 1, total, 2):
            mergedLists.append(merge(lists[i - 1], lists[i]))

        return self.mergeKLists(mergedLists)