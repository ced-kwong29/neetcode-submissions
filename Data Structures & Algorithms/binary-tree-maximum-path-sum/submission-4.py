# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.pathSum = root.val

        def dfs(tree):
            if not tree:
                return 0

            left = max(dfs(tree.left), 0)
            right = max(dfs(tree.right), 0)

            currSum = left + tree.val + right
            if currSum > self.pathSum:
                self.pathSum = currSum

            return tree.val + max(left, right)


        dfs(root)
        return self.pathSum

        
            