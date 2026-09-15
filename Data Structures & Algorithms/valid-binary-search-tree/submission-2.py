# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l = []
        def trav(node):
            if not node: return
            trav(node.left)
            l.append(node.val)
            trav(node.right)
            
        trav(root)
        
        # Check for strictly increasing elements (no duplicates)
        for i in range(1, len(l)):
            if l[i] <= l[i - 1]:
                return False
        return True