# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def insert(tree, subTree):
            if not tree:
                return subTree
            if not subTree:
                return tree

            if tree.val > subTree.val:
                tree.left = insert(tree.left, subTree)
            elif tree.val < subTree.val:
                tree.right = insert(tree.right, subTree)
            return tree

        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            root = insert(root.right, root.left)

        return root