"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        mapping = {}

        pos = head
        while pos:
            if pos not in mapping:
                mapping[pos] = Node(pos.val)
            
            if pos.next:
                if pos.next not in mapping:
                    mapping[pos.next] = Node(pos.next.val)
                
                mapping[pos].next = mapping[pos.next]
            
            if pos.random:
                if pos.random not in mapping:
                    mapping[pos.random] = Node(pos.random.val)
                
                mapping[pos].random = mapping[pos.random]
    
            pos = pos.next

        return mapping[head]