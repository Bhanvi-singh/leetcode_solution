# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxi = float('-inf')
        def solve(node):
           
            if node is None:
                return 0
            left= solve(node.left)
            if left < 0:
                 left = 0
            right = solve(node.right)
            if right < 0:
                right = 0
            self.maxi = max(self.maxi, left + node.val  + right)
            return node.val + max(left, right)
        solve(root) 
        return self.maxi
        