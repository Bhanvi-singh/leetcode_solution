# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """


        """self.count = 0
        def solve(node):
            if node is None:
                return 0 
            self.count += 1
            solve(node.left)
            solve(node.right)
        solve(root)
        return self.count """

        def solve(node):
            if node is None:
                return 0 

            left = solve(node.left)
            right = solve(node.right)
            total = left + right + 1
            return total
            
        return solve(root)        