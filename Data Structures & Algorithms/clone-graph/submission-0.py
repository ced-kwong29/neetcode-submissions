"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        cloneMap = dict()

        q = deque([node])
        while q:
            original = q.popleft()

            if original.val not in cloneMap:
                cloneMap[original.val] = Node(original.val)

            for neighbor in original.neighbors:
                if neighbor.val not in cloneMap:
                    q.append(neighbor)
                    cloneMap[neighbor.val] = Node(neighbor.val)
                
                cloneMap[original.val].neighbors.append(cloneMap[neighbor.val])

        return cloneMap[node.val]