# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def postorder(root):
            if not root:
                return -1
            left = postorder(root.left)
            right = postorder(root.right)
            self.res = max(self.res, 2+left+right)
            return 1+max(left,right)
        postorder(root)
        return self.res