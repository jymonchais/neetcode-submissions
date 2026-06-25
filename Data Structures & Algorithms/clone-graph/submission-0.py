"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        newGraph = {}
        newGraph[node] = Node(node.val)
        queue = deque([node])

        while queue:
            #remove it from queue
            curr = queue.popleft()

            for n in curr.neighbors:
                if n not in newGraph:
                    newGraph[n] = Node(n.val)
                    queue.append(n)
                newGraph[curr].neighbors.append(newGraph[n])

        return newGraph[node]