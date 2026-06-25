# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []

        def bfsHelper(node, depth):    
            if not node:
                return node

            if len(output) == depth:
                output.append([])

            output[depth].append(node.val)
            bfsHelper(node.left, depth + 1)
            bfsHelper(node.right, depth + 1)
            

        bfsHelper(root, 0)            
        return output



