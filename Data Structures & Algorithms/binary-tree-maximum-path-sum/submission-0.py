# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root : return 0
        f=float('-inf')
        def mg(node):
            nonlocal f
            if not node: return 0

            leg=max(0,mg(node.left))
            reg=max(0,mg(node.right))

            cu=node.val+leg+reg
            f=max(cu,f)

            return node.val+max(leg,reg)
        mg(root)
        return f