# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")
        def dfs(tree):
            if not tree:
                return 0

            left, right = max(dfs(tree.left), 0), max(dfs(tree.right), 0)
            currSum = left + tree.val + right

            nonlocal maxSum
            if currSum > maxSum:
                maxSum = currSum

            return tree.val + max(left, right)


        dfs(root)
        return maxSum