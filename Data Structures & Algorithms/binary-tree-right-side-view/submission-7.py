# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        queue = deque([root])

        while queue:
            rgh = None
            size = len(queue)

            for i in range(size):
                curr = queue.popleft()
                if curr:
                    rgh = curr
                    queue.append(curr.left)
                    queue.append(curr.right)
            if rgh:
                output.append(rgh.val)


        return output   