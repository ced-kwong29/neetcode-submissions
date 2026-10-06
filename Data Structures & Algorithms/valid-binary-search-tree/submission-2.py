# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(tree, minVal, maxVal):
            if not tree:
                return True

            if minVal < tree.val < maxVal:
                return validate(tree.left, minVal, tree.val) and validate(tree.right, tree.val, maxVal)

            return False

        return validate(root, float("-inf"), float("inf"))