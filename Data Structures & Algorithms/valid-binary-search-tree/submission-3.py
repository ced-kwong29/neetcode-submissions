# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(tree, minVal, maxVal):
            if not tree:
                return True

            return minVal < tree.val < maxVal and dfs(tree.left, minVal, tree.val) and dfs(tree.right, tree.val, maxVal)

        return dfs(root, float("-inf"), float("inf"))
