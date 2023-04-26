# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # Itereative DFS
        depth = 0
        stack = [[root, 1]]
        while stack:
            curr, d = stack.pop()
            if curr:
                depth = max(depth, d)
                stack.append([curr.left, d+1])
                stack.append([curr.right, d+1])
        return depth