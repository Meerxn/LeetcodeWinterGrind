"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]
            else:
                
                copiedNode = Node(node.val)
                visited[node] = copiedNode
                for n in node.neighbors:
                    copiedNode.neighbors.append(dfs(n))
                return copiedNode
        if node == None:
            return None
        else:
            return dfs(node)
        
        