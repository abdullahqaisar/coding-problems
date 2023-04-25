# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        #Iterative
        result, stack = [], []
        while stack or root:
            while root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return result
        
        
        # Recursive
        res = []
        def preorder(curr):
            if not curr:
                return
            res.append(curr.val)
            preorder(curr.left)
            preorder(curr.right)

        preorder(root)
        return res