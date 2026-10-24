# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        res = []

        q = [root]
        while q:
            level = []
            for _ in range(len(q)):
                node = q.pop(0)
                if node:
                    level.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)
                else:
                    level.append("N")
            
            while level and level[-1] == "N":
                level.pop()

            if level:
                res.append("|".join(level))

        return "_".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        q = data.split("_")
        
        root = TreeNode(int(q.pop(0)))
        prev = [root]

        while q:
            prevNdx = 0
            level, vals = [], q.pop(0).split("|")

            for i in range(len(vals)):
                node = None if vals[i] == "N" else TreeNode(int(vals[i]))

                if i % 2 == 0:
                    prev[prevNdx].left = node
                else:
                    prev[prevNdx].right = node
                    prevNdx += 1

                if node:
                    level.append(node)

            prev = level

        return root


        
