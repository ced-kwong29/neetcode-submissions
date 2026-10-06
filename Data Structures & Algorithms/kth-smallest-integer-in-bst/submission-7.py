# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root

        count = 0

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            count += 1
            if count == k:
                break

            node = stack.pop().right

        return stack[-1].val