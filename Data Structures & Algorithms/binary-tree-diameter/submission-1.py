# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def dfs(tree):
            if not tree:
                return 0

            left, right = dfs(tree.left), dfs(tree.right)
            currDiameter = left + right

            nonlocal maxDiameter
            if currDiameter > maxDiameter:
                maxDiameter = currDiameter

            return 1 + max(left, right)

        dfs(root)
        return maxDiameter

        