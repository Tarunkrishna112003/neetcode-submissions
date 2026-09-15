"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import copy

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        old_to_new = {}
        
        def dfs(curr):
            if curr in old_to_new:
                return old_to_new[curr]
                
            copy_node = Node(curr.val)
            old_to_new[curr] = copy_node
            
            # For adjList = [[]], curr.neighbors is []
            # The loop finishes without doing anything, returning Node(1) with neighbors = []
            for neighbor in curr.neighbors:
                copy_node.neighbors.append(dfs(neighbor))
                
            return copy_node
            
        return dfs(node)
        # if not node:
        #     return 
        
        # return copy.deepcopy(node)