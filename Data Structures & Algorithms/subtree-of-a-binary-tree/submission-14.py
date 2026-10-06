# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(tree1, tree2):
            if not (tree1 or tree2):
                return True

            if not (tree1 and tree2):
                return False

            return tree1.val == tree2.val and isSame(tree1.left, tree2.left) and isSame(tree1.right, tree2.right)

        if not root:
            return False

        if not subRoot or isSame(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)