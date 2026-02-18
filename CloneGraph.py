



# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {} #node to node mapping to check whether explored

        def dfs(node):

            if node in old_to_new: #if already explored, return copy
                return old_to_new[node]

            # Make a new copy, without neighbors yet
            copy = Node(node.val)
            # hash it to save for later
            old_to_new[node] = copy

            #recursively add its neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node)