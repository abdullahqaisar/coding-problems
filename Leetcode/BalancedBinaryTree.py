# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = 0
        def postorder(root):
            if not root:
                return 0
            left = postorder(root.left)
            right = postorder(root.right)
            self.res = max(self.res, abs(right-left))
            return 1+max(left,right)
        postorder(root)
        if self.res>1:
            return False
        return True