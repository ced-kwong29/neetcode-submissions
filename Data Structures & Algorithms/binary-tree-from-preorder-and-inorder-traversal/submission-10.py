# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {val: i for i, val in enumerate(inorder)}

        self.pre_ndx = 0
        def dfs(left, right):
            if left > right:
                return None

            val = preorder[self.pre_ndx]
            self.pre_ndx += 1

            root = TreeNode(val)
            root.left = dfs(left, index[val] - 1)
            root.right = dfs(index[val] + 1, right)

            return root

        return dfs(0, len(preorder) - 1)