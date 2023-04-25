# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Recrsive Solution
        def invert(curr):
            if not curr:
                return
            
            curr.left, curr.right = curr.right, curr.left
            invert(curr.left)
            invert(curr.right)
        invert(root)
        return root
        

        # Iterative Solution
        stack, visited = [root], [False]
        curr = root

        while stack:
            curr, v = stack.pop(), visited.pop()
            if curr:
                if v:
                    curr.left, curr.right = curr.right, curr.left
                else:
                    stack.append(curr)
                    visited.append(True)
                    stack.append(curr.right)
                    visited.append(False)
                    stack.append(curr.left)
                    visited.append(False)
        return root

        