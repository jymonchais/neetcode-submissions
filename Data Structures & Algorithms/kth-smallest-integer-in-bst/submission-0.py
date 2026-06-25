# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = []


        def order(node):
            if not node:
                return node

            order(node.left)
            output.append(node.val)
            order(node.right)

        order(root)

        val = output[k - 1]
        return output[k - 1]