# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        count = 0
        kthSmallest = 0

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            node = stack.pop()
            
            kthSmallest = node.val
            count += 1
            if count == k:
                break

            curr = node.right

        return kthSmallest
