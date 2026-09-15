# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return 0
        l=[]
        def ord(node):
            if not node: return
            ord(node.left)
            l.append(node.val)
            ord(node.right)
        ord(root)
        return l[k-1]